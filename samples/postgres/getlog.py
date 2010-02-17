#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

logfile=os.path.realpath(os.path.join(os.getcwd(),"cvs.log"))

cvsroot=":pserver:anoncvs@anoncvs.postgresql.org:/projects/cvsroot"
module="pgsql"

try:   
    os.mkdir(".src")
except:
    pass
os.chdir(".src")
fin,fout=os.popen2(
"""
cvs -d %(cvsroot)s login
""" % vars())
fin.write("\n")

os.system(
"""
cvs -d %(cvsroot)s checkout %(module)s
""" % vars())

os.chdir(module)

os.system(
"""
cvs log > %(logfile)s
""" % vars())
