#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
svn log --verbose --revision "{2009-11-01}:HEAD" http://svn.wikimedia.org/svnroot/mediawiki/ >svn.log
""")

