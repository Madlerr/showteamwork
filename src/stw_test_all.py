#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Run «showteamwork» for all samples in samples directory.
 If all VCSs (bzr/svn/hg/git) installed, the test must take several hours.
"""
import sys
import os
import time

def runme():
    """
    Main functionality.
    """
    exedir = os.path.realpath(os.path.join(os.path.dirname(sys.argv[0]), "../bin"))
    samplesdir = os.path.realpath(os.path.join(os.path.dirname(sys.argv[0]), "../samples"))
    if len(sys.argv)>1:
        samplesdir = os.path.realpath(sys.argv[1])
    os.chdir(samplesdir)
    for sdir in os.listdir(samplesdir):
        if os.path.isdir(sdir):
            callstr = os.path.join(exedir,"showteamwork") + " 1> stw-%s.log 2>&1" % sdir
            print "!!!!!!!!", sdir, ">>>>>>>"
            os.chdir(samplesdir)
            os.chdir(sdir)
            os.system(callstr)
            os.chdir(samplesdir)
    
if __name__ == '__main__':
    STIME = time.time()
    runme()                      
    print "It takes ", time.time() - STIME, " seconds" 
    