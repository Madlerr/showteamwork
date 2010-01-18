#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Main movie-generation utility.
"""

import sys
import os
import time
from VCSVisualizer import VCSVisualizer
from STWUtils      import file_is_ok


def guess_inputfile():
    """
    Heuristics: trying to guess input file.
    """
    vcss = {
       "CVS": {
           "logfile":    "cvs.log",
           "logcommand": "cvs log",
           "directory":  "CVS",
        },         
       "SVN": {
           "logfile":    "svn.log",
           "logcommand": "svn log -v",
           "directory":  ".svn",
        },         
       "Bazaar": {
           "logfile":    "bzr.log",
           "logcommand": "bzr log -v",
           "directory":  ".bzr",
        },         
       "GIT": {
           "logfile":    "git.log",
           "logcommand": '''git log --name-status --pretty=format:"%n------------------------------------------------------------------------%nr%h | %ae | %ai (%aD) | x lines%nChanged paths:"''',
           "directory":  ".git",
        },         
       "Mercurial": {
           "logfile":    "hg.log",
           "logcommand": "hg -v log",
           "directory":  ".hg",
        },         
    }    
    def getvcscommand( avcs ):
        """
        Interpolate command template for the given @avcs
        """
        scmd = "%(logcommand)s > %(logfile)s" % avcs
        return scmd


    if file_is_ok("activity.xml"):
        return "activity.xml"
    
    #trying to find input log file
    for vcs in vcss.values():
        if file_is_ok(vcs["logfile"]):
            return vcs["logfile"]

    #Otherwise, maybe we need to execute special script to get log file?
    if file_is_ok("getlog.py"):
        home = os.getcwd() 
        execfile("getlog.py")
        os.chdir(home)

    #another try to find input log file
    for vcs in vcss.values():
        if file_is_ok(vcs["logfile"]):
            return vcs["logfile"]

    #may be we already inside working directory for some VCS:
    for vcs in vcss.values():
        def try_to_find_dir(adir):
            """
            Try to find given dir @adir on current dir and two upper directory levels.
            """
            path = adir
            if os.path.isdir(path):
                return path
            path = "../" + path
            if os.path.isdir(path):
                return path
            path = "../" + path
            if os.path.isdir(path):
                return path
            return None
        vcsdir = try_to_find_dir(vcs["directory"])
        if vcsdir:
            os.system(getvcscommand(vcs))
            break

    #last try to find input log file
    for vcs in vcss.values():
        if file_is_ok(vcs["logfile"]):
            return vcs["logfile"]
    
    print "Hello. We support following VCS: ", vcss.keys()
    print "We are waiting for one of the following nonempty log files\n:"
    for v, vcs in vcss.items():
        scmd = getvcscommand(vcs)
        print "".join([ 'for <', v, '> we need <', vcs["logfile"], '>, so run command\n',
                       '-' * 24, '\n', scmd, '\n', '=' * 24, '\n' ])
    print "Or provide <activity.xml> file in native XML-format."
    print "Java (JRE) must be installed."
    if os.name != "nt":
        print """
        If you under Linux, you have to install following utilities:
ffmpeg, mencoder (from mplayer project), gource.
"""        
    sys.exit(0)

def runme():
    """
      Guess input file, and run main process.
    """
    
    inputfile = guess_inputfile()
    if __debug__:
        # To intercept all exceptions in IDE
        vcs = VCSVisualizer(inputfile)
        vcs.process()
    else:
        try:
            vcs = VCSVisualizer(inputfile)
            vcs.process()
        except Exception, e:
            print "".join(["Sorry:", str(e),
                          "\n---------------\n", 
                          "If you need support, mail your input file and the above error",
                          " to stanislav.fomin@gmail.com or \n report it to ",
                          " http://code.google.com/p/showteamwork/issues/ " ])
       
if __name__ == '__main__':
    STIME = time.time()
    runme()                      
    print "It takes ", time.time() - STIME, " seconds" 

