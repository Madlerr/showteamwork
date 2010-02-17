
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="cache", "cache.*", 244,251,143, 244,251,143
ColorAssign2="foreign", "foreign.*", 142,233,204, 142,233,204
ColorAssign3="layout", "layout.*", 252,169,206, 252,169,206
ColorAssign4="mapping3", "mapping3.*", 68,240,167, 68,240,167
ColorAssign5="specs", "specs.*", 230,137,57, 230,137,57
ColorAssign6="subvertpy", "subvertpy.*", 87,161,49, 87,161,49
ColorAssign7="subvertpy/subvertpy", "subvertpy/subvertpy.*", 200,63,245, 200,63,245
ColorAssign8="subvertpy/tests", "subvertpy/tests.*", 86,72,214, 86,72,214
ColorAssign9="tests", "tests.*", 60,68,224, 60,68,224
ColorAssign10="tests/mapping3", "tests/mapping3.*", 52,37,229, 52,37,229
ColorAssign11="tests/mapping_implementations", "tests/mapping_implementations.*", 64,32,79, 64,32,79
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
    

