#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system(
"""
bzr log -v lp:inkscape -r date:2010-01-01..date:today > bzr.log
""")

