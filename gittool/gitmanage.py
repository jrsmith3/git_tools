# -*- coding: utf-8 -*-

import os
import logging
import argparse
import copy
import git

def remove_remotes(repo):
    """
    Removes all remotes from git repo, `repo`.
    """
    for remote in repo.remotes:
        repo.delete_remote(remote)

def make_src_path(src):
    """
    Converts `src` to absolute (if necessary) and returns it. 
    """
    if os.path.isabs(src):
        path = src
    else:
        pwd = os.getcwd()
        path = os.path.join(pwd, src)

    return path

def make_dst_path(dst):
    """
    Create the destination path and return it.
    """
    if dst is None:
        head, src = os.path.split(self.src)
        src += "-split"
        path = os.path.join(head, src)
    else:
        if os.path.isabs(dst):
            path = dst
        else:
            pwd = os.getcwd()
            path = os.path.join(pwd, dst)

    return path

def subdir_repo_list(repo):
    """
    Return list of subdirs from `src` which will turn into repos.

    Note that this method is a little more sophisticated than just `os.listdir`. It will return only subdirectories of `src`, and only those which are not in `.gitignore` or the `.git` directory.
    """
    dir_items = os.listdir(repo.working_dir)
    ignoreds = self.ignored_list(self.repo)
    uncommitteds = self.uncommitted_list(self.repo)

    subdirs = []

    for item in dir_items:
        conditions = [os.dir.isdir(item),
                      not item.startswith("."),]

        if all(conditions):
            subdirs.append(item)

def ignored_list(repo):
    """
    Return full-path list of ignored items in repo.
    """
    ignored_string = self.repo.git.ls_files(i = True, o = True, exclude_standard = True, directory = True)
    ignoreds = []

    for ignored in ignored_string.split("\n"):
        full_path = os.path.join(repo.working_dir, ignored)
        if os.path.isdir(full_path)
            ignoreds.append(full_path)

    return ignoreds

def uncommitted_list(repo):
    """
    Return full-path list of ignored items in repo.
    """
    uncommitted_string = self.repo.git.ls_files(o = True, exclude_standard = True, directory = True)
    uncomitteds = []

    for uncomitted in uncomitted_string.split("\n"):
        full_path = os.path.join(repo.working_dir, uncomitted)
        if os.path.isdir(full_path):
            uncomitteds.append()

    return uncomitteds


class main():
    """
    Class that always gets instantiated when program is run
    """
    def __init__(self):

        parser = argparse.ArgumentParser(description='Tools for dealing with several git repos at once.')

        # Split
        # =====
        split_group = parser.add_argument_group("split")
        split_group.add_argument(
            "-s",
            "--split",
            help = "Splits a monolithic repo into individual repos.",
            metavar = "src_repo",
            )

        split_group.add_argument(
            "dst",
            help = "Location of split repos.",
            nargs = "?",
            default = None,
            )

        args = parser.parse_args()

        if args.split:
            self.src = self.make_src_path(args.split)
            self.dst = self.make_dst_path(args.dst)

            # If the source directory doesn't even exist, no sense in continuing.
            if not os.path.isdir(self.src):
                raise OSError(2, "No such file or directory.", self.src)

            self.repo = git.Repo(self.src)

            subdirs = self.subdir_repo_list(self.repo)







if __name__ == "__main__":
    main()
