
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="trunk", "/trunk.*", 84,81,103, 84,81,103
ColorAssign2="trunk/DOCS", "/trunk/DOCS.*", 18,15,247, 18,15,247
ColorAssign3="trunk/gui", "/trunk/gui.*", 56,204,232, 56,204,232
ColorAssign4="trunk/help", "/trunk/help.*", 254,243,211, 254,243,211
ColorAssign5="trunk/libass", "/trunk/libass.*", 192,63,240, 192,63,240
ColorAssign6="trunk/libmpcodecs", "/trunk/libmpcodecs.*", 210,214,75, 210,214,75
ColorAssign7="trunk/libmpdemux", "/trunk/libmpdemux.*", 142,253,250, 142,253,250
ColorAssign8="trunk/libswscale", "/trunk/libswscale.*", 26,91,20, 26,91,20
ColorAssign9="trunk/libvo", "/trunk/libvo.*", 123,75,116, 123,75,116
ColorAssign10="trunk/loader", "/trunk/loader.*", 250,163,235, 250,163,235
ColorAssign11="trunk/stream", "/trunk/stream.*", 58,28,84, 58,28,84
ColorAssign12="trunk/vidix", "/trunk/vidix.*", 153,75,45, 153,75,45
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
    

