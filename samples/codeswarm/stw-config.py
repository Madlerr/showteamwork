
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="trunk", "/trunk.*", 232,255,215, 232,255,215
ColorAssign2="trunk/code_swarm", "/trunk/code_swarm.*", 243,219,90, 243,219,90
ColorAssign3="trunk/convert_logs", "/trunk/convert_logs.*", 72,238,192, 72,238,192
ColorAssign4="trunk/data", "/trunk/data.*", 210,143,248, 210,143,248
ColorAssign5="trunk/lib", "/trunk/lib.*", 147,201,65, 147,201,65
ColorAssign6="trunk/physics_engine", "/trunk/physics_engine.*", 28,206,103, 28,206,103
ColorAssign7="trunk/prototype", "/trunk/prototype.*", 112,118,54, 112,118,54
ColorAssign8="trunk/src/codeswarm", "/trunk/src/codeswarm.*", 128,53,86, 128,53,86
ColorAssign9="trunk/src/org", "/trunk/src/org.*", 189,26,7, 189,26,7
ColorAssign10="trunk/src/org/codeswarm", "/trunk/src/org/codeswarm.*", 39,54,111, 39,54,111
ColorAssign11="trunk/src/org/codeswarm/repository", "/trunk/src/org/codeswarm/repository.*", 10,12,217, 10,12,217
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
    

