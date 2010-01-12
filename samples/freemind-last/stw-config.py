
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


ColorAssign1="Attic""/cvsroot/freemind/freemind/Attic.*" 131,251,74, 131,251,74
ColorAssign2="doc""/cvsroot/freemind/freemind/doc.*" 94,124,2, 94,124,2
ColorAssign3="doc/Attic""/cvsroot/freemind/freemind/doc/Attic.*" 221,87,235, 221,87,235
ColorAssign4="freemind""/cvsroot/freemind/freemind/freemind.*" 68,53,99, 68,53,99
ColorAssign5="freemind/common""/cvsroot/freemind/freemind/freemind/common.*" 226,255,180, 226,255,180
ColorAssign6="freemind/main""/cvsroot/freemind/freemind/freemind/main.*" 16,14,158, 16,14,158
ColorAssign7="freemind/modes""/cvsroot/freemind/freemind/freemind/modes.*" 204,202,237, 204,202,237
ColorAssign8="freemind/preferences""/cvsroot/freemind/freemind/freemind/preferences.*" 95,196,95, 95,196,95
ColorAssign9="freemind/view""/cvsroot/freemind/freemind/freemind/view.*" 22,100,28, 22,100,28
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
    

