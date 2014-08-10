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
    dirnames = list_tl_subdirs(repo.wd)

    # I know I need to throw out the `.git` from that list.
    dirnames.remove(".git")

    # I need to throw out directories no files at any nesting level. In other words, a directory can have an arbitrary number of nested directories, but no files.

    # I also know that there's a possibility the repo has subdirectories that can't be split using `git subtree split`. For example these dirs may be in .gitignore (there are other cases).

    return dirnames

def dir_to_branch(dirname):
    """
    Replaces spaces with underscore.
    """
    return dirname.replace(" ", "_")

def branches_from_subdirs(repo):
    """
    `git subtree split` each subdirectory into its own branch.
    """
    dirnames = branchable_subdirs(repo)

    for dirname in dirnames:
        # the command I need to execute is
        # `git subtree split -P subdir -b subdir`
        branch_name = dir_to_branch(dirname)
        repo.git.subtree("split", P = dirname, b = branch_name)

def make_bare_repos_from_subdirs(dst_fqpn_root, repo):
    """
    Using the subdirs found in `repo`, create bare git repos at `dst_fqpn_root`.
    """
    dirnames = branchable_subdirs(repo)
    for dirname in dirnames:
        dst_fqpn = os.path.join(dst_fqpn_root, dirname)
        repo = git.Repo.init_bare(dst_fqpn)

def push_branches_to_remotes(dst_fqpn_root, repo):
    """
    This method

    1. Creates bare git repos in `dst_fqpn_root` corresponding to the subdirs of `repo`.
    2. For each branch in `repo`, push branch to correspodning remote.
    """
    make_bare_repos_from_subdirs(dst_fqpn_root, repo)

    dirnames = branchable_subdirs(repo)

    for dirname in dirnames:
        branch_name = dir_to_branch(dirname)
        remote_url = os.path.join(dst_fqpn_root, dirname)
        
        # Set up remote
        repo.git.remote("add", "dst", remote_url)

        # Push to remote
        repo.git.push("dst", branch_name)

        # Remove remote
        repo.git.remote("rm", "dst")

