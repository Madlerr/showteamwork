
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


ColorAssign1="cache""cache.*" 70,30,173, 70,30,173
ColorAssign2="foreign""foreign.*" 253,17,93, 253,17,93
ColorAssign3="layout""layout.*" 78,248,89, 78,248,89
ColorAssign4="mapping3""mapping3.*" 194,124,96, 194,124,96
ColorAssign5="specs""specs.*" 226,228,209, 226,228,209
ColorAssign6="subvertpy""subvertpy.*" 55,22,20, 55,22,20
ColorAssign7="subvertpy/subvertpy""subvertpy/subvertpy.*" 114,253,178, 114,253,178
ColorAssign8="subvertpy/tests""subvertpy/tests.*" 224,89,10, 224,89,10
ColorAssign9="testdata""testdata.*" 122,105,168, 122,105,168
ColorAssign10="tests""tests.*" 174,18,147, 174,18,147
ColorAssign11="tests/mapping3""tests/mapping3.*" 159,249,155, 159,249,155
ColorAssign12="tests/mapping_implementations""tests/mapping_implementations.*" 11,210,59, 11,210,59
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

print config, engine    
    

