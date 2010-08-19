#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

logfile=os.path.realpath(os.path.join(os.getcwd(),"git.log"))

try:   
    os.mkdir(".src")
except:
    pass
os.chdir(".src")

try:   
    os.system(
"""
git clone git://git.kernel.org/pub/scm/git/git.git
""")
except:
    pass

os.chdir("git")

s="".join(['git log --name-status --format=medium', ' > ', logfile])
os.system(s) 
