#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
svn log --verbose http://svn.apache.org/repos/asf/subversion/trunk/ > svn.log
""")

