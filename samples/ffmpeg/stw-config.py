
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="doc", "/trunk/doc.*", 255,255,243, 255,255,243
ColorAssign2="libav", "/trunk/libav.*", 229,252,82, 229,252,82
ColorAssign3="libavcodec", "/trunk/libavcodec.*", 152,207,232, 152,207,232
ColorAssign4="libavcodec/i386", "/trunk/libavcodec/i386.*", 215,183,181, 215,183,181
ColorAssign5="libavcodec/libpostproc", "/trunk/libavcodec/libpostproc.*", 104,238,18, 104,238,18
ColorAssign6="libavcodec/ppc", "/trunk/libavcodec/ppc.*", 187,168,39, 187,168,39
ColorAssign7="libavdevice", "/trunk/libavdevice.*", 239,71,116, 239,71,116
ColorAssign8="libavfilter", "/trunk/libavfilter.*", 190,81,168, 190,81,168
ColorAssign9="libavformat", "/trunk/libavformat.*", 6,126,48, 6,126,48
ColorAssign10="libavutil", "/trunk/libavutil.*", 124,20,79, 124,20,79
ColorAssign11="tests", "/trunk/tests.*", 128,11,37, 128,11,37
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
    

