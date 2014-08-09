# -*- coding: utf-8 -*-
import os

def dict_to_fs(fs_dict, fqpn_root):
    """
    Create a directory tree in the filesystem from a dict.

    Formatting rules for `fs_dict` are as follows:

    * Keys give the file/directory name.
    * `str` values indicate the key maps to a file which contains the contents of the string.
    * `dict` values indicate the key maps to a directory which contains the contents of the dictionary as given by these rules.
    * A value which is an empty dict will create an empty directory.

    :param dict fs_dict: Specially formatted dict representing a directory tree structure.
    :param str fqpn_root: Fully qualified path name in which to create the directory tree.
    """
    if type(fs_dict) is not dict:
        raise TypeError("fs_dict must be a dictionary.")

    if type(fqpn_root) is not str:
        raise TypeError("fqpn_root must be a string.")

    for key, val in fs_dict.items():
        fq_path_name = os.path.join(fqpn_root, key)

        if type(val) is dict:
            # Create a subdirectory at this point, call `dict_to_fs`.
            os.mkdir(fq_path_name)
            dict_to_fs(val, fq_path_name)
        elif type(val) is str:
            # Create a file at this point with the contents in `val`.
            with open(fq_path_name, "w") as f:
                f.write(val)
        else:
            msg = "Values must be str or dict. Key `%s` is %s"
            subs = (key, type(val))
            raise TypeError(msg % subs)


def fs_to_dict(fqpn_root):
    """
    If I can map a dict to a directory tree, I can do the reverse.


    :param str fqpn_root: Fully qualified path name from which to create the directory tree dict.
    """
    pass
