#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
svn log --xml   --verbose --username guest http://viewvc.tigris.org/svn/viewvc/ >svn-log.xml
""")

