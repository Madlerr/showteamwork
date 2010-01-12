#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  Collection of all auxiliary utilities.
"""
import os
import time
import re

   
def getintparam(config, attrname, default):
    """
     Get int parameter value from config file like
       attrname=value
     and return «default» if the attribute does not exists.  
    """
    res = default
    re_ = re.compile(r"(?sm)%(attrname)s=(?P<%(attrname)s>[\d]+)\s*\n" % vars())
    m = re_.search(config)
    if m:
        res = int(m.group(attrname))
    return res           


def file_is_ok(filepath):
    """
      Simple checks — file ``filepath`` exists and has nonzero size.
    """
    return os.path.exists(filepath) and os.stat(filepath).st_size>0 

def createdir(dirpath):
    """
     Create directory with parent directories.
     Try to make them hidden (under Windows).
    """
    if not os.path.exists(dirpath):
        try:
            os.mkdir(dirpath)
        except OSError:
            (path, dir_) = os.path.split(dirpath)
            if dir_ != "":
                createdir(path)
                os.mkdir(dirpath)
    try:
        from win32api import SetFileAttributes
        from win32con import FILE_ATTRIBUTE_HIDDEN
        SetFileAttributes(dirpath, FILE_ATTRIBUTE_HIDDEN)
    except:
        pass


def hash4file(filepath, salt=None):
    """
     Get some HashDigest for file without reading it entirely into memory.
    """
    import hashlib
    m = hashlib.sha1()   # Perfectionist can use sha224.

    if filepath:
        block_size = 2**16     # Perfectionist can tune.
        lf = open(filepath,"r")
        while True:
            data = lf.read(block_size)
            if not data:
                break
            m.update(data)
        lf.close()
    if salt:
        m.update(salt)
    return m.hexdigest()[:16]


def unicodeanyway(astr):
    """
     Try to guess input encoding and decode input «bytes»-string to unicode string.
    """
    str_ = astr
    for encoding in "utf-8", "windows-1251", "cp866", "koi-8":
        try:
            str_ = unicode(astr.decode(encoding))
            break
        except:
            pass
    return str_    

def dateanyway(sdate):
    """
     Try to guess string date format 
    """
    date = None
    for format in ['%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M:%S', '%d %b %Y %H:%M:%S']:
        try:
            date = time.strptime(sdate.strip(), format)
            break
        except ValueError:
            pass
    if date:    
        return date
    raise Exception("Cannot guess date format for %s " % sdate)

