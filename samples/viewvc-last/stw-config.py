
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="branches", "/branches.*", 242,225,165, 242,225,165
ColorAssign2="branches/1.1.x/conf", "/branches/1.1.x/conf.*", 218,250,5, 218,250,5
ColorAssign3="branches/1.1.x/lib", "/branches/1.1.x/lib.*", 74,233,231, 74,233,231
ColorAssign4="templates-contrib", "/templates-contrib.*", 131,212,160, 131,212,160
ColorAssign5="templates-contrib/1.1", "/templates-contrib/1.1.*", 169,152,70, 169,152,70
ColorAssign6="trunk", "/trunk.*", 202,58,121, 202,58,121
ColorAssign7="trunk/bin", "/trunk/bin.*", 163,72,146, 163,72,146
ColorAssign8="trunk/conf", "/trunk/conf.*", 131,68,35, 131,68,35
ColorAssign9="trunk/lib", "/trunk/lib.*", 87,41,171, 87,41,171
ColorAssign10="trunk/viewvc.org", "/trunk/viewvc.org.*", 97,5,5, 97,5,5
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
    

