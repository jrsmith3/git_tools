# -*- coding: utf-8 -*-
"""
Herein I generate control git repos to perform tests. I want to do this programatically so its auditable.
"""

import git
import tarfile
import os
import shutil

def generate_repo_with_three_remotes():
    """
    Generates a git repo with three remotes.
    """
    remotes = {"gethub": "git@gethub.com:username/three_remotes.git",
               "example": "git@example.com:username/three_remotes.git",
               "notaurl": "git@notaurl.com:username/three_remotes.git",}

    repo_dirname = "three_remotes"
    repo_targzfilename = repo_dirname + ".tar.gz"

    # Initialize repo.
    repo = git.Repo.init(repo_dirname)

    # Add remotes.
    for name, url in remotes.iteritems():
        repo.create_remote(name, url)

    # Archive repo.
    with tarfile.open(repo_targzfilename, "w:gz") as tar:
        tar.add(repo_dirname)

    # Delete repo directory.
    shutil.rmtree(repo_dirname)

def generate_1_ignore_2_dirs_1_uncommit():
    """
    Repository with one ignored and one uncomitted file, two dirs.

    The two directories will have files which are comitted to the repo. The `.gitignore` will be the uncomitted file, and a file named `ignored` will be ignored in gitignore.
    """
    repo_dirname = "1_ignore_2_dirs_1_uncommit"
    repo_targzfilename = repo_dirname + ".tar.gz"

    # Initialize repo
    repo = git.Repo.init(repo_dirname)

    # Files that will live in the repo.
    gitignore = "ignored"
    ignored_filename = "ignored"
    dir_slug = "dir%s"

    # Make .gitignore
    filepath = os.path.join(repo_dirname, ".gitignore") 
    with open(filepath, "w") as f:
        f.write(gitignore)

    # `touch` file `ignored`
    filepath = os.path.join(repo_dirname, gitignore)
    with open(filepath,"w") as f:
        pass

    # Create the two directories with files.
    for indx in range(1,3):
        dirname = dir_slug % indx
        dirpath = os.path.join(repo_dirname, dirname)

        os.mkdir(dirpath)

        # `touch` file
        file_path = os.path.join(dirpath, "file")
        with open(file_path, "w") as f:
            pass

        # git add file
        add_path = os.path.join(dirname, "file")
        repo.git.add(add_path)

    # Commit changes.
    repo.git.commit(m = "Commit to repo.")

    # Archive repo.
    with tarfile.open(repo_targzfilename, "w:gz") as tar:
        tar.add(repo_dirname)

    # Delete repo directory.
    shutil.rmtree(repo_dirname)
