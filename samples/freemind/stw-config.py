
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="accessories/plugins", "/cvsroot/freemind/freemind/accessories/plugins.*", 243,254,248, 243,254,248
ColorAssign2="accessories", "/cvsroot/freemind/freemind/accessories.*", 215,234,164, 215,234,164
ColorAssign3="freemind/controller", "/cvsroot/freemind/freemind/freemind/controller.*", 189,163,253, 189,163,253
ColorAssign4="freemind/main", "/cvsroot/freemind/freemind/freemind/main.*", 148,186,232, 148,186,232
ColorAssign5="freemind/modes/mindmapmode/actions/Attic", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode/actions/Attic.*", 128,159,123, 128,159,123
ColorAssign6="freemind/modes/mindmapmode/actions", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode/actions.*", 154,77,192, 154,77,192
ColorAssign7="freemind/modes/mindmapmode", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode.*", 201,19,91, 201,19,91
ColorAssign8="freemind/view", "/cvsroot/freemind/freemind/freemind/view.*", 51,79,86, 51,79,86
ColorAssign9="freemind", "/cvsroot/freemind/freemind/freemind.*", 66,29,147, 66,29,147
ColorAssign10="plugins", "/cvsroot/freemind/freemind/plugins.*", 30,23,176, 30,23,176
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
    

