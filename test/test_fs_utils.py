# -*- coding: utf-8 -*-
import os
import shutil
import unittest
import gittool

test_dir_root = os.path.dirname(os.path.realpath(__file__))

class MethodsInput(unittest.TestCase):
    """
    Tests behavior of methods which take input arguments.
    """
    good_input_dict = {"dir1": {}}
    path_to_dummy_file = os.path.join(test_dir_root, "dummy.txt")

    def setUp(self):
        """
        Creates a dummy file in the `test_dir_root`.
        """
        with open(self.path_to_dummy_file, "w"):
            pass

    def tearDown(self):
        """
        Removes dummy file in the `test_dir_root`.
        """
        os.remove(self.path_to_dummy_file)

    def test_dict_to_fs_fs_dict_non_dict(self):
        """
        First argument to dict_to_fs must be a dictionary.
        """
        self.assertRaises(TypeError, gittool.fs_utils.dict_to_fs, "not a dict", test_dir_root)

    def test_dict_to_fs_fs_dict_values_non_dict_string(self):
        """
        Values of fs_dict must be either strings or dictionaries.
        """
        bad_input = {"neither_string_nor_dict": 42.}

        self.assertRaises(TypeError, gittool.fs_utils.dict_to_fs, bad_input, test_dir_root)

    def test_dict_to_fs_fqpn_root_non_str(self):
        """
        Second argument to dict_to_fs must be a string.
        """
        self.assertRaises(TypeError, gittool.fs_utils.dict_to_fs, self.good_input_dict, 42.)

    def test_dict_to_fs_fqpn_root_nonexistant_path(self):
        """
        Second arg to dict_to_fs must correspond to exitant path.
        """
        nonexistant_subdir = "does_not_exist"
        bad_fqpn_root = os.path.join(test_dir_root, nonexistant_subdir)

        self.assertRaises(OSError, gittool.fs_utils.dict_to_fs, self.good_input_dict, bad_fqpn_root)

    def test_dict_to_fs_fqpn_root_non_directory_path(self):
        """
        Second arg to dict_to_fs must correspond to a dir, not a file.
        """
        self.assertRaises(OSError, gittool.fs_utils.dict_to_fs, self.good_input_dict, self.path_to_dummy_file)


class MethodsFunctionality(unittest.TestCase):
    """
    Tests proper functionality of the methods.
    """
    scratch_dir = os.path.join(test_dir_root, "scratch")

    def setUp(self):
        """
        Creates a scratch directory for the tests.
        """
        os.mkdir(self.scratch_dir)

    def tearDown(self):
        """
        Removes the scratch dir (and its contents).
        """
        shutil.rmtree(self.scratch_dir)

    def test_dict_to_fs_filename(self):
        """
        dict_to_fs should be able to create a file with a specified filename.
        """
        fs_dict = {"dummy.txt": ""}
        gittool.fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        scratch_names = os.listdir(self.scratch_dir)

        self.assertEqual(os.listdir(self.scratch_dir), fs_dict.keys())

    def test_dict_to_fs_isfile(self):
        """
        dict_to_fs should be able to create a file.
        """
        dummy_filename = "dummy.txt"
        fs_dict = {dummy_filename: ""}
        gittool.fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        dummy_fqpn = os.path.join(self.scratch_dir, dummy_filename)

        self.assertTrue(os.path.isfile(dummy_fqpn))

    def test_dict_to_fs_empty_file(self):
        """
        An empty string should generate an empty file.
        """
        dummy_filename = "dummy.txt"
        fs_dict = {dummy_filename: ""}
        gittool.fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        dummy_fqpn = os.path.join(self.scratch_dir, dummy_filename)

        self.assertEqual(os.path.getsize(dummy_fqpn), 0)

    def test_dict_to_fs_nonempty_file(self):
        """
        A nonempty string should generate a nonempty file.
        """
        dummy_filename = "dummy.txt"
        fs_dict = {dummy_filename: "Hello world.\n"}
        gittool.fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        dummy_fqpn = os.path.join(self.scratch_dir, dummy_filename)

        self.assertTrue(os.path.getsize(dummy_fqpn) > 0)
