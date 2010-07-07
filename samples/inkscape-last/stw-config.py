
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="po", "po.*", 254,255,222, 254,255,222
ColorAssign2="share/extensions", "share/extensions.*", 254,231,104, 254,231,104
ColorAssign3="share/icons", "share/icons.*", 142,236,126, 142,236,126
ColorAssign4="share", "share.*", 171,181,247, 171,181,247
ColorAssign5="src/display", "src/display.*", 22,233,20, 22,233,20
ColorAssign6="src/extension", "src/extension.*", 164,89,254, 164,89,254
ColorAssign7="src/ui", "src/ui.*", 185,64,132, 185,64,132
ColorAssign8="src", "src.*", 247,9,21, 247,9,21
ColorAssign9="trunk/src", "trunk/src.*", 29,108,79, 29,108,79
ColorAssign10="trunk", "trunk.*", 90,29,89, 90,29,89
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
    

