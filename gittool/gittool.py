# -*- coding: utf-8 -*-
"""
gittool - Deal with many git repos at once
"""

import os
import logging
import argparse
import git


def list_tl_subdirs(src_fqpn):
    """
    List of top-level subdirectories in a repository.

    :param str src_fqpn: Fully qualified path name to source directory.
    """
    dirnames = [f for f in os.listdir(src_fqpn) if os.path.isdir(os.path.join(src_fqpn,f))]

    return dirnames


def list_empty_subdirs(src_fqpn):
    """
    List of top-level subdirectories which contain no files at any nesting level.
    """
    empty_paths = []

    for path, dirs, files in os.walk(src_fqpn):
        if ".git" in dirs:
            dirs.remove(".git")
        if ".DS_Store" in files:
            files.remove(".DS_Store")
        combo_list = dirs + files
        if not combo_list:
            empty_paths.append(path)

    return empty_paths


def branchable_subdirs(repo):
    """
    List subdir names of repo which can be branches.
    """
    dirnames = list_tl_subdirs(repo)

    # I know I need to throw out the `.git` from that list.
    dirnames.remove(".git")

    # I need to throw out directories no files at any nesting level. In other words, a directory can have an arbitrary number of nested directories, but no files.

    # I also know that there's a possibility the repo has subdirectories that can't be split using `git subtree split`. For example these dirs may be in .gitignore (there are other cases).

    return dirnames


def branches_from_subdirs(repo):
    """
    `git subtree split` each subdirectory into its own branch.
    """
    dirnames = branchable_subdirs(repo)

    for dirname in dirnames:
        # the command I need to execute is
        # `git subtree split -P subdir -b subdir`
        repo.git.subtree("split", P = dirname, b = dirname)
