#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
svn log --xml --verbose svn://svn.ffmpeg.org/ffmpeg/ > svn-log.xml
""")

