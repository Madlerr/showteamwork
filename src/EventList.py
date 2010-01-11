#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
TeamWork Events
  When/Who/Artefact/What
  
Parsing from VCS logs.
Writing to XML or custom formats.
"""

import os
import time
import re

from copy import copy
from xml.sax.saxutils   import escape
from lxml               import etree

from STWUtils           import unicodeanyway, dateanyway



def textfilter(text):
    """
      Kill emplylines, newlines, convert quotes,
      convert to unicode.
    """
    text = re.sub('^\n', '', text)
    text = text.replace("\n", ". ").replace('''"''', """'""")
    text = unicodeanyway(text)
    return text

class Event:
    """
       Unit of work: When/Who/Artefact/What
    """
    def __init__(self, filename, date, author, action="M", comment = ""):
        self.filename = unicodeanyway(filename)
        self.date     = date     # time in milliseconds
        self.action   = textfilter(action)   
        self.author   = textfilter(author)   
        self.filename = textfilter(self.filename)   
        self.comment  = textfilter(comment)

    def set_comment(self, comment=""):
        """
          Set comment.
          To-do: remove it nahren.
        """
        self.comment = textfilter(comment)
        
    def __cmp__(self, other):
        """
          compare events by date (for chronological sort)
        """
        return cmp(self.date, other.date)
 
  
class EventList:
    """
      List of TeamWork Events
          «When/Who/Artefact/What»
          
        Parsing from VCS logs.
        Writing to XML or custom formats.
    """
    def __init__(self):
        self.events = []
        self.filter_events = None
    
    def write_xml(self, filepath):
        """
          Write out the «standard» XML file with team events
        """
        lf = open(filepath,  'w')
        lf.write('''<?xml version="1.0"?>\n<file_events>\n''')
        self.events.sort()
        for event in self.events:
            ev = copy(event)
            ev.filename = escape(ev.filename)
            ev.author   = escape(ev.author)   
            ev.comment  = escape(ev.comment)
            s = u'''<event date="%(date)s" author="%(author)s"
filename="%(filename)s" comment="%(comment)s" />
''' % vars(ev)   
            lf.write(s.encode("utf-8"))
        lf.write('</file_events>\n')
        lf.close()
    
    def write_gource_custom(self, filepath):
        """
          Write out the file in «Gource Custom format» with team events
        """
        lf = open(filepath,  'w')
        self.events.sort()
        for event in self.events:
            ev = copy(event)
            ev.date = int(ev.date/1000)
            ev.filename = ev.filename.decode("utf-8")
            s = u"%(date)s|%(author)s|%(action)s|%(filename)s|\n" % vars(ev)
            lf.write(s.encode("utf-8"))
        lf.close()
    
    def read_log(self, logfilename):
        """
           Transform logs from different VCSs to standard XML.
           
           Very bad code, refactoring needed.
        """
        def get_line_value(key, default):
            """
              Parse line of the form:
                [key]:  [value]
              and return value for the given @key  
            """
            if line.startswith(key+":"):
                return line[len(key)+1:].strip()
            return default

        if not os.path.exists(logfilename):
            raise Exception("File «%s» not exists!" % logfilename)
     
        logfile = os.path.split(logfilename)[1]

        if logfile.startswith("activity") and logfile.endswith(".xml"):
            self.parse_activity_file(logfilename)
            return
        
        file_handle = open(logfilename,  'r')
        event_list = []

        if logfile in ["git.log", "svn.log"]:
            svn_sep = "-"*72
            # Todo: kill all plain SVG log parsing, keeps only XML log processing.
            # For Git change custom format, so parse it with Bazaar or other VCS logs

#Sample SVG.log
#------------------------------------------------------------------------
#r9 | glantau | 2001-07-24 00:58:31 +0400 (Вт, 24 июл 2001) | 2 lines
#Changed paths:
#   M /trunk/configure
#   M /trunk/libav/utils.c
#   M /trunk/libavcodec/Makefile
#   M /trunk/libavcodec/ac3dec.c
#   M /trunk/libavcodec/avcodec.h
#   M /trunk/libavcodec/utils.c
#
#added CONFIG_AC3, CONFIG_MPGLIB, CONFIG_DECODERS and CONFIG_ENCODERS 
#
#------------------------------------------------------------------------
#r1 | (no author) | 2000-12-20 03:02:47 +0300 (Ср, 20 дек 2000) | 1 line
#Changed paths:
#   A /trunk
#
#New repository initialized by cvs2svn.
#------------------------------------------------------------------------
            
            line = file_handle.readline()
            while len(line) > 0:
                # The svn_sep indicates a new revision history to parse.
                if line.startswith(svn_sep):
                    try:
                        event_list_commit = []
                        rev_line = file_handle.readline()
                        if rev_line is '' or len(rev_line) < 2:
                            break
                        rev_parts = rev_line.split(' | ')
                        author = rev_parts[1]
                        date_parts = rev_parts[2].split(" ")
                        date = date_parts[0] + " " + date_parts[1]
                        date = time.strptime(date, '%Y-%m-%d %H:%M:%S')
                        date = int(time.mktime(date))*1000
                        
                        # Skip the 'Changed paths:' line and start reading in the changed filenames.
                        path = file_handle.readline()
                        path = file_handle.readline()
                        while len(path) > 1:
                            ch_path = None
                            action_ = "A"
                            if logfile == "svn.log":
                                action_  = path[:5].strip()
                                ch_path = path[5:].split(" (from")[0].replace("\n", "")
                            else:
                                # git uses quotes if filename contains unprintable characters
                                action_  = path[:2].strip()
                                ch_path = path[2:].replace("\n", "").replace("\"", "")
                            event_list_commit.append(Event(ch_path, date, author, action=action_))
                            path = file_handle.readline()
                        line = file_handle.readline()
                        comment = ""
                        while not line.startswith(svn_sep) and len(line)>0:
                            comment += line
                            line = file_handle.readline()
                        for e in event_list_commit:
                            e.set_comment(comment)
                        event_list += event_list_commit
                    except:
                        line = file_handle.readline()
                        continue
                else:    
                    line = file_handle.readline()
    
        elif logfile in ["cvs.log"]:
            filename = ""
            line = file_handle.readline()
            while len(line) > 0:
                # a new revision history to parse.
                if line.startswith("----------------------------"):
                    #Read the revision number
                    rev_line = file_handle.readline()
    
                    # Extract author and date from revision line.
                    rev_line = file_handle.readline()
                    if rev_line.startswith("date:"):
                        cvsaction = "M"
                        if rev_line.lower().find("state: dead;")>0:
                            cvsaction = "D"
                        if rev_line.lower().find("state: exp;")>0 and \
                           rev_line.lower().find("lines:")<0:   
                            cvsaction = "A"
                        
                        rev_parts = rev_line.split(';  ')
                        date_parts = rev_parts[0].split(": ")
                        date_without_plus = date_parts[1].split("+")
                        date = dateanyway(date_without_plus[0])
                        date = int(time.mktime(date))*1000
                        author = rev_parts[1].split(": ")[1]
                        ev = Event(filename, date, author, action=cvsaction)
                        comment = ""
                        while True:
                            line = file_handle.readline()
                            if line.startswith("-" * 16) or line.startswith("=" * 16):
                                break
                            comment += line.strip().replace("\n", " ")
                        ev.set_comment(comment)    
                        event_list.append(ev)
                elif(line.lower().find("rcs file: ") >= 0):
                    rev_line = line.split(": ")
                    filename = rev_line[1].strip().split(',')[0]
                    line = file_handle.readline()
                else:
                    line = file_handle.readline()
            
        elif logfile in ["hg.log"]:
# Sample:
#changeset:   2:ecf3fd948051
#user:        mpm@selenic.com
#date:        Tue May 03 18:35:03 2005 -0800
#files:       mercurial/revlog.py
#description:
#Handle nullid better for ancestor
#
#
#changeset:   1:273ce12ad8f1
#user:        mpm@selenic.com
#date:        Tue May 03 13:27:13 2005 -0800
#files:       .hgignore README
#description:
#Update README to discuss remote pull, rsync, and the hg repo
#add a .hgignore file

# !!!Problem: I do not know how to get action type (add/delete/modify)
#              for modified files in hg.log
            messagemode = False
            filesmode = False
            author = ""
            timestamp = ""
            action = "M"
            message = ""
            for line in file_handle.readlines():
                if get_line_value("changeset", False):
                    author = ""
                    timestamp = ""
                    files = ""
                    lastmessage = ""
                if messagemode:
                    if line.strip() == "" and lastmessage == "":
                        messagemode = False
                    lastmessage = line.strip()
                    message += " " + lastmessage
                    if not messagemode:
                        for filename in files.split():
                            e = Event(filename, date, author, action)
                            e.set_comment(message)
                            event_list.append(e)
                author = get_line_value("user", author)
                timestamp = get_line_value("date", timestamp)
                if timestamp != "":
                    tm = time.strptime(timestamp[4:-6], '%b %d %H:%M:%S %Y')
                    date = int(time.mktime(tm) * 1000)
                files = get_line_value("files", files)
                if line.startswith("description:"):
                    message = ""
                    messagemode = True
    
        elif logfile in ["bzr.log"]:
# Sample:            
#------------------------------------------------------------
#revno: 2
#author:    Stas Fomin
#committer: mbp@sourcefrog.net
#timestamp: Wed 2005-03-09 04:09:29 +0000
#message:
#  add python bytecode to default ignore pattern
#modified:
#  bzrlib/__init__.py
#------------------------------------------------------------
#revno: 1
#committer: mbp@sourcefrog.net
#timestamp: Wed 2005-03-09 04:08:15 +0000
#message:
#  import from baz patch-364
#added:
#  README
#  bzr.py
#  bzrlib/
#  bzrlib/__init__.py
#------------------------------------------------------------
            messagemode = False
            filesmode = False
            author = ""
            timestamp = ""
            action = "M"
            for line in file_handle.readlines():
                if get_line_value("revno", False):
                    author = None
                    timestamp = ""
                    action = "M"
                if not line.startswith("  "):
                    messagemode = False
                    filesmode = False
                if messagemode:
                    message += " " + line.strip()            
                if filesmode:
                    filename = line.strip()
                    e = Event(filename, date, author, action)
                    e.set_comment(message)
                    event_list.append(e)
                author = get_line_value("author", author)
                if not author:
                    author = get_line_value("committer", author)
                timestamp = get_line_value("timestamp", timestamp)
                if timestamp != "":
                    tm = time.strptime(timestamp[4:-6], '%Y-%m-%d %H:%M:%S')
                    date = int(time.mktime(tm) * 1000)
                if line.startswith("message:"):
                    message = ""
                    messagemode = True
                if line.startswith("modified:"):
                    filesmode = True
                    action = "M"
                if line.startswith("added:"):
                    filesmode = True
                    action = "A"
                if line.startswith("deleted:"):
                    filesmode = True
                    action = "D"
           
        file_handle.close()
        
        if self.filter_events:
            for ev in event_list:
                if self.filter_events(ev):
                    self.events.append(ev)
        else:            
            self.events = event_list
            
    def parse_activity_file(self, activitypath):
        """
          Get events from ``activity.xml``
        """
        lf = open(activitypath)   
        doc = etree.parse(lf)
        lf.close()
        root = doc.getroot() 
        if not root.tag == "file_events":
            raise Exception("Root tag of projects.xml must be «file_events»")

        for event in root:
            assert(event.tag == "event")
            filename = event.get("filename")
            date = event.get("date")
            author = event.get("author")
            comment = ''
            if "comment" in event:
                comment = event.get("comment")
            action = 'M'
            if "action" in event:
                action = event.get("action")
            ev = Event(filename, date, author, action, comment)
            ok = True
            if self.filter_events:
                ok = self.filter_events(ev)
            if ok:    
                self.events.append(ev)          