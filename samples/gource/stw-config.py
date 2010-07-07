
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="contrib", "contrib.*", 226,215,246, 226,215,246
ColorAssign2="data", "data.*", 144,219,24, 144,219,24
ColorAssign3="data/fonts", "data/fonts.*", 77,160,218, 77,160,218
ColorAssign4="debian", "debian.*", 193,75,237, 193,75,237
ColorAssign5="dev", "dev.*", 203,53,144, 203,53,144
ColorAssign6="dev/bin", "dev/bin.*", 32,114,177, 32,114,177
ColorAssign7="m4", "m4.*", 87,30,150, 87,30,150
ColorAssign8="src", "src.*", 80,57,9, 80,57,9
ColorAssign9="src/core", "src/core.*", 98,35,52, 98,35,52
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
Width=1280
Height=720
    """

GOURCE=1
CODESWARM=1

print config, engine    
    

