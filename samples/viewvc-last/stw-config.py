
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


ColorAssign1="branches""/branches.*" 239,244,186, 239,244,186
ColorAssign2="branches/1.0.x""/branches/1.0.x.*" 70,239,156, 70,239,156
ColorAssign3="branches/1.1.x""/branches/1.1.x.*" 226,95,157, 226,95,157
ColorAssign4="tags""/tags.*" 14,159,103, 14,159,103
ColorAssign5="templates-contrib""/templates-contrib.*" 178,37,50, 178,37,50
ColorAssign6="templates-contrib/1.1""/templates-contrib/1.1.*" 17,13,193, 17,13,193
ColorAssign7="trunk""/trunk.*" 199,234,76, 199,234,76
ColorAssign8="trunk/bin""/trunk/bin.*" 109,21,110, 109,21,110
ColorAssign9="trunk/conf""/trunk/conf.*" 211,115,232, 211,115,232
ColorAssign10="trunk/lib""/trunk/lib.*" 123,103,28, 123,103,28
ColorAssign11="trunk/templates""/trunk/templates.*" 22,68,241, 22,68,241
ColorAssign12="trunk/viewvc.org""/trunk/viewvc.org.*" 252,42,49, 252,42,49
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
    

