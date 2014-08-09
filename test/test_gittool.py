# -*- coding: utf-8 -*-
import os
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
    pass
