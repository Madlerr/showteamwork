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
import trans

from copy import copy
from xml.sax.saxutils   import escape
from lxml               import etree

from STWUtils           import unicodeanyway, dateanyway



def textfilter(text):
    """
      Kill emplylines, newlines, convert quotes,
      convert to unicode.
    """
    text = unicodeanyway(text)
    if type(text) != type(u""):
        return u""
    text = re.sub('^\n', '', text)
    text = text.replace("\n", ". ").replace('''"''', """'""")
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
            s = u'''<event
  date="%(date)s"  author="%(author)s"  filename="%(filename)s"
        action="%(action)s" comment="%(comment)s" />
''' % vars(ev)   
            lf.write(s.encode("trans"))
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
            ev.date = long(ev.date)/1000
            ev.filename = unicodeanyway(ev.filename)
            s = u"%(date)s|%(author)s|%(action)s|%(filename)s|\n" % vars(ev)
            lf.write(s.encode("trans"))
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

        def parse_svn_xml_log(file_handle):
            """
              Read messages from ``svnxmlpath``
            """
            doc = etree.parse(file_handle)
            root = doc.getroot() 
            if root.tag != "log":
                raise Exception("Root tag of svn-log.xml must be <log>")
                
            for logentry in root:
                paths_ = []
                for x in logentry:
                    comment_ = ""
                    if x.tag == "author":
                        author_ = x.text        
                    elif x.tag == "date":
                        date_ = x.text
                        if date_.find(".")>0:
                            date_ = date_.split(".")[0]
                        date_ = time.strptime(date_, '%Y-%m-%dT%H:%M:%S')
                        date_ = int(time.mktime(date_))*1000
                    elif x.tag == "msg":
                        comment_ = x.text        
                    elif x.tag == "paths":
                        paths_ = x
                        
                for p in paths_:
                    path_ = p.text
                    action_ = p.get("action")
                    event_list.append(Event(path_, date_, author_, action=action_, comment=comment_))

        def parse_mediawiki_xml(file_handle):
            """
              Read messages from ``mediawiki.xml``
            """
            doc = etree.parse(file_handle)
            root = doc.getroot()
            ns = "{http://www.mediawiki.org/xml/export-0.4/}"
            if root.tag != ns + "mediawiki":
                raise Exception("Root tag of svn-log.xml must be <mediawiki>")
            for page in root.iter(ns+"page"):
                for title in page.iter(ns+"title"):
                    path_ =  unicodeanyway(title.text).encode("trans")
                    break
                action_ = 'A'
                for revision in page.iter(ns+"revision"):
                    for contributor in revision.iter(ns+"contributor"):
                        for username in contributor.iter(ns+"username"):
                            author_ = username.text
                            break
                        break
                    for timestamp in revision.iter(ns+"timestamp"):
                        date_  =  timestamp.text
                        date_ = time.strptime(date_, '%Y-%m-%dT%H:%M:%SZ')
                        date_ = int(time.mktime(date_))*1000
                        break
                    comment_ = ""
                    for comment in revision.iter(ns+"comment"):
                        comment_ =  unicodeanyway(comment.text).encode("utf8")
                        if action_ == 'A':
                            comment_ = unicodeanyway(title.text).encode("utf8")  
                        break
                    event_list.append(Event(path_, date_, author_, action = action_, comment=comment_))
                    action_ = 'M'


        if not os.path.exists(logfilename):
            raise Exception("File <%s> not exists!" % logfilename)
     
        logfile = os.path.split(logfilename)[1]

        if logfile.startswith("activity") and logfile.endswith(".xml"):
            self.parse_activity_file(logfilename)
            return
        
        file_handle = open(logfilename,  'r')
        event_list = []

        if logfile in ["svn-log.xml"]:
            parse_svn_xml_log(file_handle)

        if logfile in ["mediawiki.xml"]:
            parse_mediawiki_xml(file_handle)
            
        if logfile in ["git.log"]:
            line = file_handle.readline()
            newcommit_re = re.compile("commit [0-9a-f]+$")
            path_re = re.compile("(?P<action>(M|A|D))\t(?P<path>.+)$")
            messagemode = False
            while len(line) > 0:
                if newcommit_re.match(line):
                    path_    = ""
                    date_    = ""
                    author_  = ""
                    action_  = ""
                    comment_ = ""
                    messagemode = False
                if line.startswith('Author:'):
                    author_ = get_line_value('Author', author_)
                elif line.startswith('Date:'):
                    date_ = get_line_value('Date', date_)
                    date_ = date_[-26:-6].strip()
                    date_ = time.strptime(date_, '%b %d %H:%M:%S %Y')
                    date_ = int(time.mktime(date_))*1000
                    messagemode = True
                else:    
                    is_path = path_re.match(line)    
                    if messagemode:    
                        if is_path:
                            messagemode = False
                        else:    
                            comment_ += line
                    if not messagemode and is_path:
                        action_ = is_path.group("action")
                        path_   = is_path.group("path")
                        ev = Event(path_, date_, author_, action=action_)
                        ev.set_comment(comment_)    
                        event_list.append(ev)
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
            raise Exception("Root tag of projects.xml must be <file_events>")

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