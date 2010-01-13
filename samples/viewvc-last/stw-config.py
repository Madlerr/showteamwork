
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="branches", "/branches.*", 158,133,29, 158,133,29
ColorAssign2="branches/1.0.x", "/branches/1.0.x.*", 134,21,158, 134,21,158
ColorAssign3="branches/1.1.x", "/branches/1.1.x.*", 78,223,39, 78,223,39
ColorAssign4="tags", "/tags.*", 192,230,154, 192,230,154
ColorAssign5="templates-contrib", "/templates-contrib.*", 25,31,100, 25,31,100
ColorAssign6="templates-contrib/1.1", "/templates-contrib/1.1.*", 223,40,79, 223,40,79
ColorAssign7="trunk", "/trunk.*", 254,237,255, 254,237,255
ColorAssign8="trunk/bin", "/trunk/bin.*", 211,162,226, 211,162,226
ColorAssign9="trunk/conf", "/trunk/conf.*", 97,220,253, 97,220,253
ColorAssign10="trunk/lib", "/trunk/lib.*", 192,14,2, 192,14,2
ColorAssign11="trunk/templates", "/trunk/templates.*", 91,7,233, 91,7,233
ColorAssign12="trunk/viewvc.org", "/trunk/viewvc.org.*", 193,152,90, 193,152,90
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
    

