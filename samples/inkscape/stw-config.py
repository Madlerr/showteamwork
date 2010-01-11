
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


ColorAssign1="po""po.*" 175,33,251, 175,33,251
ColorAssign2="share""share.*" 36,244,202, 36,244,202
ColorAssign3="share/extensions""share/extensions.*" 165,246,169, 165,246,169
ColorAssign4="share/icons""share/icons.*" 40,39,157, 40,39,157
ColorAssign5="src""src.*" 110,170,53, 110,170,53
ColorAssign6="src/display""src/display.*" 254,255,237, 254,255,237
ColorAssign7="src/dom""src/dom.*" 39,106,34, 39,106,34
ColorAssign8="src/extension""src/extension.*" 65,13,38, 65,13,38
ColorAssign9="src/live_effects""src/live_effects.*" 203,163,111, 203,163,111
ColorAssign10="src/ui""src/ui.*" 91,169,76, 91,169,76
ColorAssign11="trunk""trunk.*" 22,111,188, 22,111,188
ColorAssign12="trunk/src""trunk/src.*" 7,142,203, 7,142,203
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
    

