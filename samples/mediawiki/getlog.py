#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
svn log --verbose http://svn.wikimedia.org/svnroot/mediawiki/ > svn.log
""")

