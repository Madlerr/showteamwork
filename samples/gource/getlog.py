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

s="".join(['git log --name-status ',
'--pretty=format:"%n------------------------------------------------------------------------%nr%h | %ae | %ai (%aD) | x lines%nChanged paths:" ',
' > ', logfile])

os.system(s)
