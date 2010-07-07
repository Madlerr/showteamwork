
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="Attic", "/cvsroot/freemind/freemind/Attic.*", 245,242,251, 245,242,251
ColorAssign2="doc", "/cvsroot/freemind/freemind/doc.*", 181,231,151, 181,231,151
ColorAssign3="doc/Attic", "/cvsroot/freemind/freemind/doc/Attic.*", 176,217,137, 176,217,137
ColorAssign4="freemind", "/cvsroot/freemind/freemind/freemind.*", 205,128,247, 205,128,247
ColorAssign5="freemind/common", "/cvsroot/freemind/freemind/freemind/common.*", 190,153,153, 190,153,153
ColorAssign6="freemind/modes/mindmapmode", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode.*", 99,171,12, 99,171,12
ColorAssign7="freemind/modes/mindmapmode/actions", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode/actions.*", 205,56,96, 205,56,96
ColorAssign8="freemind/modes/mindmapmode/actions/Attic", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode/actions/Attic.*", 131,57,127, 131,57,127
ColorAssign9="freemind/modes/mindmapmode/actions/xml", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode/actions/xml.*", 143,32,1, 143,32,1
ColorAssign10="freemind/modes/mindmapmode/actions/xml/Attic", "/cvsroot/freemind/freemind/freemind/modes/mindmapmode/actions/xml/Attic.*", 59,19,61, 59,19,61
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
    

