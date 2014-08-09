# -*- coding: utf-8 -*-
from distutils.core import setup

setup(name = 'git_tool',
      version = '0.0.1',
      author = 'Joshua Ryan Smith',
      author_email = 'joshua.r.smith@gmail.com',
      packages = ['gittool'],
      url = 'https://github.com/jrsmith3/git_tools',
      description = 'tools for managing many git repositories',
      classifiers = ["Programming Language :: Python",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                     "Development Status :: 2 - Pre-Alpha",
                     "Intended Audience :: Developers",
                     "Topic :: Software Development :: Version Control",
                     "Topic :: Utilities",
                     "Natural Language :: English",],
      install_requires = ['GitPython'],)