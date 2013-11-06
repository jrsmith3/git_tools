import gittool
import unittest
import gittool

class test_list_git_repos(unittest.TestCase):

    # Bad input
    # ---------
    def test_directory_wrong_type(self):
        """
        TypeError when `directory` is not str.
        """
        self.assertRaises(TypeError, gittool.list_git_repos, 12.8)

    def test_directory_doesnt_exist(self):
        """
        OSError when `directory` doesn't exist in the filesystem.
        """
        not_a_dir = "this string is in no way a directory !@(*$^&@%^#"
        self.assertRaises(OSError, gittool.list_git_repos,not_a_dir)

    def test_bare_not_boolean(self):
        """
        Pretty much any python object coerces to a boolean value. 
        This test is moot.
        """
        pass

    # Method functionality
    # --------------------
    def test_bare_repos(self):
        """
        Return list of bare repos by default.
        """
        known_bare_repos = ["1_bare.git", "2_bare.git"]
        returned_bare_repos = gittool.list_git_repos("test")
        self.assertEqual(sorted(known_bare_repos), sorted(returned_bare_repos))

    def test_all_repos(self):
        """
        Return all git repos when param bare = False
        """
        pass

    def test_returned_elements_arent_paths(self):
        """
        The returned list's elements shouldn't be full or partial paths.
        """
        pass
