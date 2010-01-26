#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime

begindate=(datetime.date.today()-datetime.timedelta(days=14)).strftime("%Y-%m-%d")
os.system(
"""
svn log --verbose --revision "{%(begindate)s}:HEAD" http://svn.wikimedia.org/svnroot/mediawiki/ >svn.log
""" % vars())

