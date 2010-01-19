#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Clean all samples (test) directories
"""

import sys
import os
from STWUtils import removedirorfile

def runme():
    """
    Main process with cleaning
    """
    samplesdir = os.path.realpath(os.path.join(os.path.dirname(sys.argv[0]), "../samples"))
    os.chdir(samplesdir)
    for sample in os.listdir(samplesdir):
        if os.path.isdir(sample):
            print "Cleaning dir", sample, ">>>>>>>"
            os.chdir(samplesdir)
            os.chdir(sample)
            for p in os.listdir("."):
                if p != "getlog.py" and p not in ["stw-config.py",
                                                  "stw-filter-events.py",
                                                  "stw-scenario.txt",
                                                  "stw-config.py"]:
                    if os.path.isdir(p):
                        removedir(p)
                    else:    
                        os.unlink(p)
            os.chdir(samplesdir)
    
if __name__ == '__main__':
    runme()
 