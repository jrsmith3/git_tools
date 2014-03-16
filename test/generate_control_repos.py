# -*- coding: utf-8 -*-
"""
Herein I generate control git repos to perform tests. I want to do this programatically so its auditable.
"""

import git
import tarfile

def generate_repo_with_three_remotes():
    """
    Generates a git repo with three remotes.
    """
    remotes = {"gethub": "git@gethub.com:username/three_remotes.git",
               "example": "git@example.com:username/three_remotes.git",
               "notaurl": "git@notaurl.com:username/three_remotes.git",}

    repo_dirname = "three_remotes"
    repo_targzfilename = repo_dirname + ".tar.gz"

    # Initialize repo
    repo = git.Repo.init(repo_dirname)

    # Add remotes
    for name, url in remotes.iteritems():
        repo.create_remote(name, url)

    # Archive repo.
    with tarfile.open(repo_targzfilename, "w:gz") as tar:
        tar.add(repo_dirname)
