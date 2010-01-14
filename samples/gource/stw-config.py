
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="contrib", "contrib.*", 223,66,204, 223,66,204
ColorAssign2="data", "data.*", 206,238,238, 206,238,238
ColorAssign3="data/fonts", "data/fonts.*", 185,254,115, 185,254,115
ColorAssign4="debian", "debian.*", 121,174,162, 121,174,162
ColorAssign5="dev", "dev.*", 112,78,90, 112,78,90
ColorAssign6="dev/bin", "dev/bin.*", 91,251,84, 91,251,84
ColorAssign7="m4", "m4.*", 89,98,143, 89,98,143
ColorAssign8="src", "src.*", 54,22,164, 54,22,164
ColorAssign9="src/core", "src/core.*", 24,169,168, 24,169,168
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
    

