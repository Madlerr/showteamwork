#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
svn log --xml  --verbose http://codeswarm.googlecode.com/svn/trunk/ > svn-log.xml
""")

