
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="/trunk/doc", "/trunk/doc.*", 17,32,147, 17,32,147
ColorAssign2="/trunk/libav", "/trunk/libav.*", 24,210,134, 24,210,134
ColorAssign3="/trunk/libavcodec", "/trunk/libavcodec.*", 39,239,141, 39,239,141
ColorAssign4="/trunk/libavcodec/i386", "/trunk/libavcodec/i386.*", 57,180,123, 57,180,123
ColorAssign5="/trunk/libavcodec/libpostproc", "/trunk/libavcodec/libpostproc.*", 93,77,213, 93,77,213
ColorAssign6="/trunk/libavcodec/ppc", "/trunk/libavcodec/ppc.*", 126,29,171, 126,29,171
ColorAssign7="/trunk/libavdevice", "/trunk/libavdevice.*", 174,17,57, 174,17,57
ColorAssign8="/trunk/libavfilter", "/trunk/libavfilter.*", 177,254,218, 177,254,218
ColorAssign9="/trunk/libavformat", "/trunk/libavformat.*", 208,218,82, 208,218,82
ColorAssign10="/trunk/libavutil", "/trunk/libavutil.*", 230,206,65, 230,206,65
ColorAssign11="/trunk/tests", "/trunk/tests.*", 253,141,114, 253,141,114
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
    

