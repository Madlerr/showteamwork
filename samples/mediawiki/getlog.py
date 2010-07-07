#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
svn log --xml   --verbose http://svn.wikimedia.org/svnroot/mediawiki/trunk/ > svn-log.xml
""")

