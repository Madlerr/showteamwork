#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime

begindate=(datetime.date.today()-datetime.timedelta(days=14)).strftime("%Y-%m-%d")
os.system(
"""
svn log --xml  --verbose --revision "{%(begindate)s}:HEAD" http://svn.wikimedia.org/svnroot/mediawiki/trunk/ >svn-log.xml
""" % vars())

