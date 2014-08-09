# -*- coding: utf-8 -*-
import os
import unittest
import gittool

test_dir_root = os.path.dirname(os.path.realpath(__file__))

class MethodsInput(unittest.TestCase):
    """
    Tests behavior of methods which take input arguments.
    """
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

    


class MethodsFunctionality(unittest.TestCase):
    """
    Tests proper functionality of the methods.
    """
    pass
