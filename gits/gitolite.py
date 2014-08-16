# -*- coding: utf-8 -*-
"""
Utilities for gitolite.
"""
import os
import git

def gen_gitolite_conf_entry(dirname, key_alias, permissions = "RW+"):
    """
    Generates gitolite conf entry for a repo.

    :param str dirname: Relative or absolute path to a directory containing a git repository.
    :param str key_alias: SSH key alias name.
    :param str permissions: Permissions associated with SSH key.
    """
    slug = "repo\t%s\n\t%s\t=   %s\n"
    basename = os.path.basename(dirname)
    return slug % (basename, permissions, key_alias)

def gen_gitolite_conf_entries(dirnames, key_alias, permissions = "RW+"):
    """
    Generates gitolite conf entries for several repos at once.

    :param list dirnames: Relative or absolute paths to directories containing git repositories.
    :param str key_alias: SSH key alias name.
    :param str permissions: Permissions associated with SSH key.
    """
    conf_entries = ""
    for dirname in dirnames:
        conf_entries += gen_gitolite_conf_entry(dirname, key_alias, permissions)
        conf_entries += "\n"

    return conf_entries
