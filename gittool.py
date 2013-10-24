# -*- coding: utf-8 -*-
"""
gittool - Deal with many git repos at once
"""

import os
import logging
import argparse
import copy
from gittle import Gittle
from dulwich.errors import NotGitRepository

def print_files(group_name, paths):
    # I copied this from https://github.com/FriendCode/gittle/blob/master/examples/status.py
    if not paths:
        return
    sorted_paths = sorted(paths)
    print("\n%s :" % group_name)
    print('\n'.join(sorted_paths))


def clone_all(repos_source, repos_dest = None):
    """
    Clone all bare git repos from a location in the filesysem
    """
    if repos_dest is None:
        repos_dest = os.getcwd()

    # Is the destination directory actually in the filesystem?
    if not os.path.isdir(repos_dest):
        raise OSError(0, "Repos dest. directory not found", directory)

    repos = self.list_git_repos(repos_source)
    for repo in repos:
        bare_repo_name = os.path.basename(repo)
        repo_name = os.path.splitext(bare_repo_name)[0]
        repo_path = os.path.join(repos_dest, repo_name)

        print "Cloning", repo
        print "     to", repo_path
        Gittle.clone(repo, repo_path)


def list_git_repos(directory, bare = True):
    """
    Return list of git repos in specified directory

    :param str directory: Location in which to search for git repos
    :param bool bare: If true, return list of repos which are bare. Otherwise, return full list of repos found in `directory`. Default = True.
    """
    # Is directory actually in the filesystem?
    if not os.path.isdir(directory):
        raise OSError(0, "Repos source directory not found", directory)

    # Return a list of subdirectories of the directory specified in `directory`.
    subdirs = os.walk(directory).next()[1]

    all_repos = []
    bare_repos = []
    for subdir in subdirs:
        try:
            subdir_path = os.path.join(directory, subdir)
            repo = Gittle(subdir_path)

            all_repos.append(subdir_path)
            if repo.is_bare:
                bare_repos.append(subdir_path)

        except NotGitRepository:
            pass

    if bare:
        return bare_repos
    else:
        return all_repos

def branch_status(repo):
    """
    Returns a string of information about the active branch & origin.

    This method returns the following information about the active branch and the remote origin:

    * Name of active branch.
    * Existance of remote origin.
    * If the active branch is ahead/behind origin or if the two have diverged.

    :param gittle.Gittle repo: Git repository object.
    """
    active_branch_msg = "On branch: %s\n" % repo.active_branch

def get_origin_branch_name(repo):
    """
    Returns string 'origin/<active branch name>'
    """
    return "origin/%s" % repo.active_branch


def origin_message(repo):
    """
    Returns a string regarding the existance of the remote origin.

    :param gittle.Gittle repo: Git repository object.
    """
    origin_branch_name = self.get_origin_branch_name(repo)

    if origin_branch_name in repo.remote_branches:
        origin_branch_msg = ""
    else:
        origin_branch_msg = "No %s\n" % origin_branch_name

    return origin_branch_msg

def get_branch_commits_as_shas(repo, origin = False):
    """
    Return commit history of branch as a list of sha strings.

    :param gittle.Gittle repo: Git repository object.
    :param bool origin: True returns branch of origin. False returns local branch. Default = False.
    """
    if origin:
        branch_name = get_origin_branch_name(repo)
        branch_sha = repo.remote_branches[branch_name]
    else:
        branch_sha = repo.branches[repo.active_branch]

    branch_commits = repo.ref_walker(branch_sha)
    branch_shas = commits_to_shas(branch_commits)

    return branch_shas

def commits_to_shas(commits):
    """
    Converts the list from branch_walker to a list of sha id strings.
    """
    shas = []
    for commit in commits:
        shas.append(commit.id)

    return shas

def truncate_shas_lists(active_branch_shas, origin_branch_shas):
    """
    Return lists with common end sequence removed.

    :param list active_branch_shas: List of sha id strings for the commits of the active branch.
    :param list origin_branch_shas: List of sha id strings for the commits of the branch on origin corresponding to the active branch.
    """
    # The logic here is to reverse both lists, then zip iterate over the pair, popping off identical items. At the end, reverse the resulting two lists and return them.
    active_shas = copy.copy(active_branch_shas)
    origin_shas = copy.copy(origin_branch_shas)

    active_shas.reverse()
    origin_shas.reverse()

    # This algorithm could probably be more elegant.
    for active_sha, origin_sha in zip(active_shas, origin_shas):
        if active_sha == origin_sha:
            active_shas.pop(0)
            origin_shas.pop(0)

    # Flip the lists back around.
    active_shas.reverse()
    origin_shas.reverse()

    return active_shas, origin_shas


def active_branch_relative_to_origin_message(repo):
    """
    Returns string describing relation between branch and origin.

    :param gittle.Gittle repo: Git repository object.
    """
    active_branch_shas = get_branch_commits_as_shas(repo)
    origin_branch_shas = get_branch_commits_as_shas(repo, True)





class main():
    """
    Class that always gets instantiated when program is run
    """

    def __init__(self):

        parser = argparse.ArgumentParser(description='Tools for dealing with several git repos at once.')


    def stat_all(self, directory):
        """
        Stats about repos in the current directory.
        """
        repo_dirs = list_git_repos(directory, bare = False)
        for repo_dir in repo_dirs:
            repo = Gittle(repo_dir)
            print "Repo", directory

            # Untracked files.
            self.print_files("Untracked files", repo.untracked_files)

            # Files changed, not yet staged for commit.
            if repo.has_commits:
                self.print_files("Changes not staged", repo.modified_unstaged_files)
            else:
                print("Initial commit.")

            # Files staged, not yet committed.
            self.print_files("Changes staged for commit", repo.pending_files - repo.untracked_files)

            # Local repo has no origin or origin/<BRANCH>
            print "Current branch:", repo.active_branch

            origin_branch = "origin/" + repo.active_branch

            if "origin" not in repo.remotes:
                print directory, "has no remote origin."
                return
            elif origin_branch not in repo.remote_branches:
                print "No branch", repo.active_branch, "in remote origin."

            # Local repo differs from remote repo.
            active_sha = repo.active_sha
            origin_branch_sha = repo.remote_branches[origin_branch]

            # List of commits of both the active branch and branch on origin.
            active_branch_walker = repo.ref_walker(active_sha)
            origin_branch_walker = repo.ref_walker(origin_branch_sha)

            active_branch_shas = commits_to_shas(active_branch_walker)
            origin_shas = commits_to_shas(origin_branch_walker)

            reduced_active_br_shas, reduced_origin_shas = \
                reduce_lists(active_branch_shas, origin_shas)
