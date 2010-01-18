
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="accessories", "/cvsroot/freemind/freemind/accessories.*", 246,254,251, 246,254,251
ColorAssign2="accessories/plugins", "/cvsroot/freemind/freemind/accessories/plugins.*", 226,215,155, 226,215,155
ColorAssign3="freemind", "/cvsroot/freemind/freemind/freemind.*", 83,235,43, 83,235,43
ColorAssign4="freemind/controller", "/cvsroot/freemind/freemind/freemind/controller.*", 152,118,21, 152,118,21
ColorAssign5="freemind/main", "/cvsroot/freemind/freemind/freemind/main.*", 143,93,132, 143,93,132
ColorAssign6="freemind/modes/mindmapmode", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode.*", 97,60,232, 97,60,232
ColorAssign7="freemind/modes/mindmapmode/actions", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode/actions.*", 198,26,70, 198,26,70
ColorAssign8="freemind/modes/mindmapmode/actions/Attic", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode/actions/Attic.*", 67,57,168, 67,57,168
ColorAssign9="freemind/view", "/cvsroot/freemind/freemind/freemind/view.*", 6,40,142, 6,40,142
ColorAssign10="plugins", "/cvsroot/freemind/freemind/plugins.*", 33,11,147, 33,11,147
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
    

