# -*- coding: utf-8 -*-
"""
gittool - Deal with many git repos at once
"""

import os
import logging
import argparse
import git

def branchable_subdirs(repo):
    """
    List subdir names of repo which can be branches.
    """
    src_fqpn = repo.wd

    dirnames = [f for f in os.listdir(src_fqpn) if os.path.isdir(os.path.join(src_fqpn,f))]

    # I know I need to throw out the `.git` from that list.
    dirnames.remove(".git")

    # I also know that there's a possibility the repo has subdirectories that can't be split using `git subtree split`. For example these dirs may be in .gitignore (there are other cases).

    return dirnames
