
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="cache", "cache.*", 30,174,42, 30,174,42
ColorAssign2="foreign", "foreign.*", 62,239,117, 62,239,117
ColorAssign3="layout", "layout.*", 99,49,98, 99,49,98
ColorAssign4="mapping3", "mapping3.*", 210,226,90, 210,226,90
ColorAssign5="specs", "specs.*", 27,10,178, 27,10,178
ColorAssign6="subvertpy", "subvertpy.*", 229,245,252, 229,245,252
ColorAssign7="subvertpy/subvertpy", "subvertpy/subvertpy.*", 107,152,210, 107,152,210
ColorAssign8="subvertpy/tests", "subvertpy/tests.*", 116,97,5, 116,97,5
ColorAssign9="testdata", "testdata.*", 223,252,12, 223,252,12
ColorAssign10="tests", "tests.*", 174,201,210, 174,201,210
ColorAssign11="tests/mapping3", "tests/mapping3.*", 159,92,165, 159,92,165
ColorAssign12="tests/mapping_implementations", "tests/mapping_implementations.*", 59,240,145, 59,240,145
"""

#Below you need to set variables «config» and «engine» (needed for CodeSwarm only)

engine="""
# name of the engine class
name=PhysicsEngineSimple

# parameters specific to this engine
edgeMultiplier=1.0
speedMultiplier=1.0
nodesMultiplier=100.0
drag=0.05
    """

draft=0
if draft:
    config+="""
Width=640
Height=480
DrawNamesHalos=false
ShowEdges=false
    """
else:
    config+="""
Width=640
Height=640
    """

GOURCE=1
CODESWARM=1

print config, engine    
    

