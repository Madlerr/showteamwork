#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
svn log --verbose --username guest http://viewvc.tigris.org/svn/viewvc/ >svn.log
""")

