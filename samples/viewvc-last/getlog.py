#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
svn log  --verbose --xml --revision "{2009-09-01}:HEAD" --verbose --username guest http://viewvc.tigris.org/svn/viewvc/ >svn-log.xml
""")

