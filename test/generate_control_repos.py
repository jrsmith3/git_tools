# -*- coding: utf-8 -*-
"""
Herein I generate control git repos to perform tests. I want to do this programatically so its auditable.
"""

import git

def generate_repo_with_three_remotes():
    """
    Generates a git repo with three remotes.
    """
    remotes = {"gethub": "git@gethub.com:username/three_remotes.git",
               "example": "git@example.com:username/three_remotes.git",
               "notaurl": "git@notaurl.com:username/three_remotes.git",}

    repo_dirname = "three_remotes"
    repo_tarfilename = repo_dirname + ".tar"

    # Initialize repo
    repo = git.Repo.init(repo_dirname)

    # Add remotes
    for name, url in remotes.keys():
        repo.create_remote(name, url)

    # Archive repo.
    repo.archive(open(repo_tarfilename, "w"))