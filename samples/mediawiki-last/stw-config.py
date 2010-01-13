
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="branches", "/branches.*", 197,31,124, 197,31,124
ColorAssign2="branches/REL1_14", "/branches/REL1_14.*", 168,130,207, 168,130,207
ColorAssign3="branches/REL1_15", "/branches/REL1_15.*", 226,247,217, 226,247,217
ColorAssign4="branches/js2-work", "/branches/js2-work.*", 254,192,73, 254,192,73
ColorAssign5="branches/new-installer", "/branches/new-installer.*", 16,75,98, 16,75,98
ColorAssign6="branches/wmf-deployment", "/branches/wmf-deployment.*", 189,108,15, 189,108,15
ColorAssign7="tags", "/tags.*", 20,3,207, 20,3,207
ColorAssign8="tags/extensions", "/tags/extensions.*", 123,207,132, 123,207,132
ColorAssign9="trunk", "/trunk.*", 102,67,209, 102,67,209
ColorAssign10="trunk/extensions", "/trunk/extensions.*", 34,96,237, 34,96,237
ColorAssign11="trunk/phase3", "/trunk/phase3.*", 165,109,31, 165,109,31
ColorAssign12="trunk/tools", "/trunk/tools.*", 248,140,81, 248,140,81
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
    

