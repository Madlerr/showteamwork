
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


ColorAssign1="Attic""/cvsroot/freemind/freemind/Attic.*" 10,188,104, 10,188,104
ColorAssign2="accessories""/cvsroot/freemind/freemind/accessories.*" 19,69,5, 19,69,5
ColorAssign3="accessories/plugins""/cvsroot/freemind/freemind/accessories/plugins.*" 147,42,169, 147,42,169
ColorAssign4="freemind""/cvsroot/freemind/freemind/freemind.*" 125,188,223, 125,188,223
ColorAssign5="freemind/controller""/cvsroot/freemind/freemind/freemind/controller.*" 164,251,90, 164,251,90
ColorAssign6="freemind/extensions""/cvsroot/freemind/freemind/freemind/extensions.*" 240,248,193, 240,248,193
ColorAssign7="freemind/main""/cvsroot/freemind/freemind/freemind/main.*" 60,217,49, 60,217,49
ColorAssign8="freemind/modes""/cvsroot/freemind/freemind/freemind/modes.*" 23,149,44, 23,149,44
ColorAssign9="freemind/view""/cvsroot/freemind/freemind/freemind/view.*" 73,140,238, 73,140,238
ColorAssign10="images""/cvsroot/freemind/freemind/images.*" 142,246,59, 142,246,59
ColorAssign11="lib""/cvsroot/freemind/freemind/lib.*" 142,216,250, 142,216,250
ColorAssign12="plugins""/cvsroot/freemind/freemind/plugins.*" 109,119,57, 109,119,57
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
    

