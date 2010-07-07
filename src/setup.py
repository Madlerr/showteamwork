#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Rebuilding executable using distutils.
"""

from distutils.core import setup
import py2exe
import os

DISTDIR = os.path.realpath(os.path.join(os.getcwd(),"../bin"))

setup(
    console = ['showteamwork.py', 'stw_test_all.py', 'stw_clean_tests.py'],
    author_email = "stanislav.fomin@gmail.com",
    options = {
        'py2exe': {
            'packages' : ['lxml', 'gzip', 'shutil', 'trans'],
            'dist_dir' : DISTDIR,    
        }
    }
    ) 