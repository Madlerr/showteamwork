
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="tags", "/tags.*", 253,172,143, 253,172,143
ColorAssign2="tags/prototype", "/tags/prototype.*", 38,170,110, 38,170,110
ColorAssign3="trunk", "/trunk.*", 87,39,87, 87,39,87
ColorAssign4="trunk/code_swarm", "/trunk/code_swarm.*", 161,186,47, 161,186,47
ColorAssign5="trunk/convert_logs", "/trunk/convert_logs.*", 210,250,230, 210,250,230
ColorAssign6="trunk/data", "/trunk/data.*", 250,8,104, 250,8,104
ColorAssign7="trunk/dist", "/trunk/dist.*", 32,5,177, 32,5,177
ColorAssign8="trunk/eclipse", "/trunk/eclipse.*", 217,236,86, 217,236,86
ColorAssign9="trunk/lib", "/trunk/lib.*", 203,26,120, 203,26,120
ColorAssign10="trunk/physics_engine", "/trunk/physics_engine.*", 172,254,160, 172,254,160
ColorAssign11="trunk/prototype", "/trunk/prototype.*", 110,208,208, 110,208,208
ColorAssign12="trunk/src", "/trunk/src.*", 151,59,148, 151,59,148
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
    

