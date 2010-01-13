
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="Attic", "/cvsroot/freemind/freemind/Attic.*", 238,38,215, 238,38,215
ColorAssign2="accessories", "/cvsroot/freemind/freemind/accessories.*", 76,231,132, 76,231,132
ColorAssign3="accessories/plugins", "/cvsroot/freemind/freemind/accessories/plugins.*", 172,5,109, 172,5,109
ColorAssign4="freemind", "/cvsroot/freemind/freemind/freemind.*", 233,195,250, 233,195,250
ColorAssign5="freemind/controller", "/cvsroot/freemind/freemind/freemind/controller.*", 2,60,15, 2,60,15
ColorAssign6="freemind/extensions", "/cvsroot/freemind/freemind/freemind/extensions.*", 254,254,160, 254,254,160
ColorAssign7="freemind/main", "/cvsroot/freemind/freemind/freemind/main.*", 33,194,199, 33,194,199
ColorAssign8="freemind/modes", "/cvsroot/freemind/freemind/freemind/modes.*", 101,103,18, 101,103,18
ColorAssign9="freemind/view", "/cvsroot/freemind/freemind/freemind/view.*", 196,11,11, 196,11,11
ColorAssign10="images", "/cvsroot/freemind/freemind/images.*", 4,210,39, 4,210,39
ColorAssign11="lib", "/cvsroot/freemind/freemind/lib.*", 254,60,136, 254,60,136
ColorAssign12="plugins", "/cvsroot/freemind/freemind/plugins.*", 228,160,13, 228,160,13
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
    

