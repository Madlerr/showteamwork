#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Clean all samples (test) directories
"""

import sys
import os
import shutil
import errno
import stat

def handle_remove_readonly(func, path, exc):
    """
    To kill read-only files.
    """
    excvalue = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
        func(path)
    else:
        raise


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
                        shutil.rmtree(p, ignore_errors=False, onerror=handle_remove_readonly)
                    else:    
                        os.unlink(p)
            os.chdir(samplesdir)
    
if __name__ == '__main__':
    runme()
 