#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import optparse
#import requests
import subprocess
import pyparsing

def main():
  usage = "usage: %prog [options] remotes_dir"
  parser = optparse.OptionParser()
  
  parser.add_option("-c","--clone", 
    help="Clone all git repos found in remotes_dir to pwd [default].",
    action="store",
    type="string",
    dest="remotes_dir",
    default=True)
  
  (options, args) = parser.parse_args()
  
  if options.remotes_dir:
    remotes = git_remotes_list(args[0])
    
    for remote in remotes:
      remote_url = "file://" + args[0] + remote
      
      print "Cloning", remote
      proc = subprocess.Popen(["git", "clone", remote_url],
        stdout = subprocess.PIPE)
      proc.wait()
      print "\r"

def git_remotes_list(remotes_dir):
  """
  Returns list of git remotes in `dirname`.
  """
  # Return a list of subdirectories of the directory specified in `remotes_dir`.
  subdirs = os.walk(remotes_dir).next()[1]
  
  remotes = []
  for subdir in subdirs:
    # Test if subdir is a git repo.
    proc = subprocess.Popen(["git", "rev-parse", "--git-dir"],
      cwd = remotes_dir + subdir,
      stdout = subprocess.PIPE,
      stderr = subprocess.PIPE)
    proc.wait()
    
    if not proc.returncode:
      # returncode = 0 and therefore this thing is a git repo.
      remotes.append(subdir)
      
  return remotes
 


if __name__ == "__main__":
  main()
  