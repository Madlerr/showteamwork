
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="Attic", "/cvsroot/freemind/freemind/Attic.*", 185,229,15, 185,229,15
ColorAssign2="doc", "/cvsroot/freemind/freemind/doc.*", 150,95,148, 150,95,148
ColorAssign3="doc/Attic", "/cvsroot/freemind/freemind/doc/Attic.*", 89,21,33, 89,21,33
ColorAssign4="freemind", "/cvsroot/freemind/freemind/freemind.*", 249,248,132, 249,248,132
ColorAssign5="freemind/common", "/cvsroot/freemind/freemind/freemind/common.*", 229,9,38, 229,9,38
ColorAssign6="freemind/main", "/cvsroot/freemind/freemind/freemind/main.*", 11,230,150, 11,230,150
ColorAssign7="freemind/modes", "/cvsroot/freemind/freemind/freemind/modes.*", 60,142,227, 60,142,227
ColorAssign8="freemind/preferences", "/cvsroot/freemind/freemind/freemind/preferences.*", 71,241,68, 71,241,68
ColorAssign9="freemind/view", "/cvsroot/freemind/freemind/freemind/view.*", 147,34,106, 147,34,106
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
    

