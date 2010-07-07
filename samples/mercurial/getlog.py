#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

logfile=os.path.realpath(os.path.join(os.getcwd(),"hg.log"))

try:   
    os.mkdir(".src")
except:
    pass
os.chdir(".src")

os.system(
"""
hg clone http://selenic.com/repo/hg
""")

os.chdir("hg")

os.system(r"hg log -v  > " + logfile) 
