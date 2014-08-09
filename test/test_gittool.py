# -*- coding: utf-8 -*-
import os
import shutil
import unittest
import gittool

# Variable containing the fully qualified path name of the directory containing these tests.
test_dir_root = os.path.dirname(os.path.realpath(__file__))


class MethodsReturnType(unittest.TestCase):
    """
    Tests output types of the methods.
    """
    def test_list_tl_subdirs(self):
        """
        list_tl_subdirs should return a list.
        """
        self.assertIsInstance(gittool.list_tl_subdirs(test_dir_root), list)

    def test_list_empty_subdirs(self):
        """
        list_empty_subdirs should return a list.
        """
        self.assertIsInstance(gittool.list_empty_subdirs(test_dir_root), list)


class MethodsReturnValues(unittest.TestCase):
    """
    Tests output values of the methods where applicable.
    """
    scratch_dir = os.path.join(test_dir_root, "scratch")

    tl_dirs = ["level1_dir1",
               "level1_dir2",
               "level1_dir3",]
    tl_dirs_contents = [{},
                        {"level2_dir1":{}},
                        {"contains_file":""},]

    tl_files = ["level1_file1"]
    tl_files_contents = [""]

    fs_dict = dict(zip(tl_dirs + tl_files, tl_dirs_contents + tl_files_contents))

    def setUp(self):
        """
        Creates nested directory structure for the tests in this class.
        """
        os.mkdir(self.scratch_dir)
        gittool.fs_utils.dict_to_fs(self.fs_dict, self.scratch_dir)

    def tearDown(self):
        """
        Cleans up nested directory structure for the tests in this class.
        """
        shutil.rmtree(self.scratch_dir)

    def test_list_tl_subdirs(self):
        """
        list_tl_subdirs should return a list with all subdirs.
        """
        pass
