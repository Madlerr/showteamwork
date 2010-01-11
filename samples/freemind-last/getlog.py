#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import datetime

logfile=os.path.realpath(os.path.join(os.getcwd(),"cvs.log"))

cvsroot=":pserver:anonymous@freemind.cvs.sourceforge.net:/cvsroot/freemind"
module="freemind"

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

fromdate=(datetime.date.today()+datetime.timedelta(days=-31*3)).strftime("%Y-%m-%d")

os.system(
"""
cvs log -d">%(fromdate)s" > %(logfile)s
""" % vars())
