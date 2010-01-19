#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Rebuilding executable using distutils.
"""

import os
import datetime
import tempfile
from STWUtils import removedirorfile

HOMEDIR = os.getcwd()
STWDIR = os.path.realpath(os.path.join(os.getcwd(),".."))

def do():
    def run(s):
        print s
        os.system(s)

    dt = datetime.date.today().strftime("%Y-%m-%d")
    tempdir = tempfile.gettempdir()
    distrdir = os.path.join(tempdir, "".join(["stw-distr-",dt]))
    if os.path.exists(distrdir):
        removedirorfile(distrdir) 

    os.chdir(STWDIR)
    s = "".join(["hg archive ", distrdir])
    run(s)
    os.chdir(distrdir)
    removedirorfile([".hg_archival.txt", ".hgignore"]) 
    
    os.mkdir("bin")
    os.chdir("src")
    run("python setup.py py2exe ")
    removedirorfile("build")

    os.chdir(distrdir)
    run("7z a -r -tzip showteamwork.zip * ")
    os.chdir(HOMEDIR)
    
    distr=os.path.join(distrdir,"showteamwork.zip")
    if not os.path.exists(distrdir):
        print "cannot find ", distr
    else:
        print "OK"  
        print distr
    
if __name__ == '__main__':
    do()   
