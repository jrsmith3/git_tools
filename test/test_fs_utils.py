# -*- coding: utf-8 -*-
import os
import shutil
import unittest
from gittool import fs_utils

test_dir_root = os.path.dirname(os.path.realpath(__file__))

class MethodsInput(unittest.TestCase):
    """
    Tests behavior of methods which take input arguments.
    """
    scratch_dir = os.path.join(test_dir_root, "scratch")
    path_to_dummy_file = os.path.join(scratch_dir, "dummy.txt")

    good_input_dict = {"dir1": {}}

    def setUp(self):
        """
        Creates the scratch dir.
        Creates a dummy file in the scratch dir.
        """
        os.mkdir(self.scratch_dir)
        with open(self.path_to_dummy_file, "w"):
            pass

    def tearDown(self):
        """
        Removes scratch dir and contents.
        """
        shutil.rmtree(self.scratch_dir)

    def test_dict_to_fs_fs_dict_non_dict(self):
        """
        First argument to dict_to_fs must be a dictionary.
        """
        self.assertRaises(TypeError, fs_utils.dict_to_fs, "not a dict", self.scratch_dir)

    def test_dict_to_fs_fs_dict_values_non_dict_string(self):
        """
        Values of fs_dict must be either strings or dictionaries.
        """
        bad_input = {"neither_string_nor_dict": 42.}

        self.assertRaises(TypeError, fs_utils.dict_to_fs, bad_input, self.scratch_dir)

    def test_dict_to_fs_fqpn_root_non_str(self):
        """
        Second argument to dict_to_fs must be a string.
        """
        self.assertRaises(TypeError, fs_utils.dict_to_fs, self.good_input_dict, 42.)

    def test_dict_to_fs_fqpn_root_string(self):
        """
        Second argument to dict_to_fs can be str.
        """
        try:
            fs_utils.dict_to_fs(self.good_input_dict, str(self.scratch_dir))
        except:
            self.fail("An exception was raised, so this method can't handle strings.")

    def test_dict_to_fs_fqpn_root_unicode(self):
        """
        Second argument to dict_to_fs can be unicode.
        """
        try:
            fs_utils.dict_to_fs(self.good_input_dict, unicode(self.scratch_dir))
        except:
            self.fail("An exception was raised, so this method can't handle unicode.")

    def test_dict_to_fs_fqpn_root_nonexistant_path(self):
        """
        Second arg to dict_to_fs must correspond to exitant path.
        """
        nonexistant_subdir = "does_not_exist"
        bad_fqpn_root = os.path.join(self.scratch_dir, nonexistant_subdir)

        self.assertRaises(OSError, fs_utils.dict_to_fs, self.good_input_dict, bad_fqpn_root)

    def test_dict_to_fs_fqpn_root_non_directory_path(self):
        """
        Second arg to dict_to_fs must correspond to a dir, not a file.
        """
        self.assertRaises(OSError, fs_utils.dict_to_fs, self.good_input_dict, self.path_to_dummy_file)


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
        fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        scratch_names = os.listdir(self.scratch_dir)

        self.assertEqual(scratch_names, fs_dict.keys())

    def test_dict_to_fs_isfile(self):
        """
        dict_to_fs should be able to create a file.
        """
        dummy_filename = "dummy.txt"
        fs_dict = {dummy_filename: ""}
        fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        dummy_fqpn = os.path.join(self.scratch_dir, dummy_filename)

        self.assertTrue(os.path.isfile(dummy_fqpn))

    def test_dict_to_fs_empty_file(self):
        """
        An empty string should generate an empty file.
        """
        dummy_filename = "dummy.txt"
        fs_dict = {dummy_filename: ""}
        fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        dummy_fqpn = os.path.join(self.scratch_dir, dummy_filename)

        self.assertEqual(os.path.getsize(dummy_fqpn), 0)

    def test_dict_to_fs_nonempty_file(self):
        """
        A nonempty string should generate a nonempty file.
        """
        dummy_filename = "dummy.txt"
        fs_dict = {dummy_filename: "Hello world.\n"}
        fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        dummy_fqpn = os.path.join(self.scratch_dir, dummy_filename)

        self.assertTrue(os.path.getsize(dummy_fqpn) > 0)

    def test_dict_to_fs_isdir(self):
        """
        dict_to_fs should be able to create a directory.
        """
        dummy_dirname = "dummy"
        fs_dict = {dummy_dirname: {}}
        fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        dummy_fqpn = os.path.join(self.scratch_dir, dummy_dirname)

        self.assertTrue(os.path.isdir(dummy_fqpn))

    def test_dict_to_fs_dir_isempty(self):
        """
        dict_to_fs should be able to create an empty directory.
        """
        dummy_dirname = "dummy"
        fs_dict = {dummy_dirname: {}}
        fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        dummy_fqpn = os.path.join(self.scratch_dir, dummy_dirname)

        should_be_empty_list = os.listdir(os.path.join(self.scratch_dir, dummy_dirname))

        self.assertEqual(should_be_empty_list, [])

    def test_dict_to_fs_dir_nonempty(self):
        """
        dict_to_fs should be able to create a populated directory.
        """
        dummy_dirname = "dummy"
        fs_dict = {dummy_dirname: {"test_file.txt":""}}
        fs_utils.dict_to_fs(fs_dict, self.scratch_dir)

        dummy_fqpn = os.path.join(self.scratch_dir, dummy_dirname)

        should_not_be_empty_list = os.listdir(os.path.join(self.scratch_dir, dummy_dirname))

        self.assertTrue(len(should_not_be_empty_list) > 0)
