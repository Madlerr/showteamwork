#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

logfile=os.path.realpath(os.path.join(os.getcwd(),"cvs.log"))

try:   
    os.mkdir(".src")
except:
    pass
os.chdir(".src")
fin,fout=os.popen2(
"""
cvs -d :pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot login
""")
fin.write("\n")

os.system(
"""
cvs -d :pserver:anonymous@cvs-mirror.mozilla.org:/cvsroot checkout mozilla/webtools/bugzilla
""")

os.chdir("mozilla/webtools/bugzilla")

os.system(
"""
cvs log > %(logfile)s
""" % vars())
