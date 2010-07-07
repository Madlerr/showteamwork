
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="branches", "/branches.*", 213,10,18, 213,10,18
ColorAssign2="branches/1.0.x", "/branches/1.0.x.*", 249,75,242, 249,75,242
ColorAssign3="branches/1.1.x", "/branches/1.1.x.*", 34,250,206, 34,250,206
ColorAssign4="templates-contrib", "/templates-contrib.*", 241,241,29, 241,241,29
ColorAssign5="templates-contrib/1.0", "/templates-contrib/1.0.*", 64,149,6, 64,149,6
ColorAssign6="templates-contrib/1.1", "/templates-contrib/1.1.*", 43,11,154, 43,11,154
ColorAssign7="trunk", "/trunk.*", 255,247,232, 255,247,232
ColorAssign8="trunk/cgi", "/trunk/cgi.*", 79,72,189, 79,72,189
ColorAssign9="trunk/lib", "/trunk/lib.*", 254,20,150, 254,20,150
ColorAssign10="trunk/templates", "/trunk/templates.*", 247,164,9, 247,164,9
ColorAssign11="trunk/viewvc.org", "/trunk/viewvc.org.*", 93,44,87, 93,44,87
ColorAssign12="trunk/website", "/trunk/website.*", 69,33,139, 69,33,139
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
    

