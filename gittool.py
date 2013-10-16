# -*- coding: utf-8 -*-
"""
gittool - Deal with many git repos at once
"""

import os
import logging
import argparse
from gittle import Gittle
from dulwich.errors import NotGitRepository

class main():
    """
    Class that always gets instantiated when program is run
    """

    def __init__(self):
        pass
        

    def clone_all(self, repos_source, repos_dest = None):
        """
        Clone all bare git repos from a location in the filesysem
        """
        if repos_dest is None:
            repos_dest = os.getcwd()

        # Is the destination directory actually in the filesystem?
        if not os.path.isdir(repos_dest):
            raise OSError(0, "Repos dest. directory not found", directory)

        repos = self.list_bare_git_repos(repos_source)
        for repo in repos:
            bare_repo_name = os.path.basename(repo)
            repo_name = os.path.splitext(bare_repo_name)[0]
            repo_path = os.path.join(repos_dest, repo_name)

            print "Cloning", repo
            print "     to", repo_path
            Gittle.clone(repo, repo_path)


    def list_bare_git_repos(self, directory):
        """
        Return list of bare git repos in specified directory
        """
        # Is directory actually in the filesystem?
        if not os.path.isdir(directory):
            raise OSError(0, "Repos source directory not found", directory)

        # Return a list of subdirectories of the directory specified in `directory`.
        subdirs = os.walk(directory).next()[1]

        repos = []
        for subdir in subdirs:
            try:
                subdir_path = os.path.join(directory, subdir)
                repo = Gittle(subdir_path)

                if repo.is_bare:
                    repos.append(subdir_path)

            except NotGitRepository:
                pass

        return repos
