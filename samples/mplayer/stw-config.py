
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


ColorAssign1="trunk""/trunk.*" 89,139,31, 89,139,31
ColorAssign2="trunk/DOCS""/trunk/DOCS.*" 17,83,90, 17,83,90
ColorAssign3="trunk/gui""/trunk/gui.*" 230,170,150, 230,170,150
ColorAssign4="trunk/help""/trunk/help.*" 218,107,240, 218,107,240
ColorAssign5="trunk/libass""/trunk/libass.*" 211,255,45, 211,255,45
ColorAssign6="trunk/libmpcodecs""/trunk/libmpcodecs.*" 242,255,246, 242,255,246
ColorAssign7="trunk/libmpdemux""/trunk/libmpdemux.*" 33,1,212, 33,1,212
ColorAssign8="trunk/libswscale""/trunk/libswscale.*" 95,70,166, 95,70,166
ColorAssign9="trunk/libvo""/trunk/libvo.*" 165,121,207, 165,121,207
ColorAssign10="trunk/loader""/trunk/loader.*" 183,78,75, 183,78,75
ColorAssign11="trunk/stream""/trunk/stream.*" 231,20,3, 231,20,3
ColorAssign12="trunk/vidix""/trunk/vidix.*" 77,183,18, 77,183,18
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
    

