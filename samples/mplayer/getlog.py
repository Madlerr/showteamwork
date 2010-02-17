#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
svn log --verbose svn://svn.mplayerhq.hu/mplayer/ > svn.log
""")

