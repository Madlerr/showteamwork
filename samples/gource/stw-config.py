
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""
GOURCE=1
CODESWARM=1


ColorAssign1="contrib""contrib.*" 249,244,6, 249,244,6
ColorAssign2="data""data.*" 40,9,249, 40,9,249
ColorAssign3="data/fonts""data/fonts.*" 56,143,160, 56,143,160
ColorAssign4="debian""debian.*" 129,208,110, 129,208,110
ColorAssign5="dev""dev.*" 59,95,47, 59,95,47
ColorAssign6="dev/bin""dev/bin.*" 250,254,255, 250,254,255
ColorAssign7="m4""m4.*" 95,215,25, 95,215,25
ColorAssign8="src""src.*" 8,162,251, 8,162,251
ColorAssign9="src/core""src/core.*" 51,212,73, 51,212,73
"""

#Below you need to set variables «config» and «engine» (needed for CodeSwarm only)

engine="""
# name of the engine class
name=PhysicsEngineSimple

# parameters specific to this engine
edgeMultiplier=1.0
speedMultiplier=1.0
nodesMultiplier=100.0
drag=0.1
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

print config, engine    
    

