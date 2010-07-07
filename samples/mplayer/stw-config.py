
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="trunk", "/trunk.*", 253,244,171, 253,244,171
ColorAssign2="trunk/DOCS/man", "/trunk/DOCS/man.*", 83,253,250, 83,253,250
ColorAssign3="trunk/DOCS/xml", "/trunk/DOCS/xml.*", 212,142,51, 212,142,51
ColorAssign4="trunk/gui", "/trunk/gui.*", 16,222,128, 16,222,128
ColorAssign5="trunk/help", "/trunk/help.*", 106,121,156, 106,121,156
ColorAssign6="trunk/libmpcodecs", "/trunk/libmpcodecs.*", 88,78,213, 88,78,213
ColorAssign7="trunk/libmpdemux", "/trunk/libmpdemux.*", 162,38,190, 162,38,190
ColorAssign8="trunk/libswscale", "/trunk/libswscale.*", 9,114,187, 9,114,187
ColorAssign9="trunk/libvo", "/trunk/libvo.*", 245,2,120, 245,2,120
ColorAssign10="trunk/stream", "/trunk/stream.*", 7,55,229, 7,55,229
ColorAssign11="trunk/vidix", "/trunk/vidix.*", 1,47,31, 1,47,31
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
    

