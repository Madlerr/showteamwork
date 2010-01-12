
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


ColorAssign1="branches""/branches.*" 222,15,80, 222,15,80
ColorAssign2="branches/1.0.x""/branches/1.0.x.*" 224,68,244, 224,68,244
ColorAssign3="branches/1.1.x""/branches/1.1.x.*" 230,211,197, 230,211,197
ColorAssign4="templates-contrib""/templates-contrib.*" 10,52,155, 10,52,155
ColorAssign5="templates-contrib/1.0""/templates-contrib/1.0.*" 109,240,118, 109,240,118
ColorAssign6="templates-contrib/1.1""/templates-contrib/1.1.*" 140,201,6, 140,201,6
ColorAssign7="trunk""/trunk.*" 88,125,94, 88,125,94
ColorAssign8="trunk/cgi""/trunk/cgi.*" 195,255,246, 195,255,246
ColorAssign9="trunk/lib""/trunk/lib.*" 183,185,15, 183,185,15
ColorAssign10="trunk/templates""/trunk/templates.*" 144,36,156, 144,36,156
ColorAssign11="trunk/viewvc.org""/trunk/viewvc.org.*" 156,194,72, 156,194,72
ColorAssign12="trunk/website""/trunk/website.*" 99,6,255, 99,6,255
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
    

