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
    os.system("git clone git://github.com/acaudwell/Gource.git")
except:
    pass

os.chdir("Gource")
os.system("git pull")

s="".join(['git log --name-status --format=medium', ' > ', logfile])

print s
os.system(s)
