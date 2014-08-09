# -*- coding: utf-8 -*-
import os

def dict_to_fs(fs_dict, fqpn_root):
    """
    Create a directory tree in the filesystem from a dict.

    Formatting rules for `fs_dict` are as follows:

    * Keys give the file/directory name.
    * `None` values indicate the key maps to an empty directory.
    * `str` values indicate the key maps to a file which contains the contents of the string.
    * `dict` values indicate the key maps to a directory which contains the contents of the dictionary as given by these rules.

    :param dict fs_dict: Specially formatted dict representing a directory tree structure.
    :param str fqpn_root: Fully qualified path name in which to create the directory tree.
    """
    for key, val in fs_dict.items():
        if val is None:
            pass
        elif type(val) is str:
            pass
        elif type(val) is dict:
            pass
        else:
            raise TypeError("Values must be None, str, or dict.")


def fs_to_dict(fqpn_root):
    """
    If I can map a dict to a directory tree, I can do the reverse.


    :param str fqpn_root: Fully qualified path name from which to create the directory tree dict.
    """
    pass
