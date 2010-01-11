
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


ColorAssign1="tags""/tags.*" 231,214,30, 231,214,30
ColorAssign2="tags/prototype""/tags/prototype.*" 45,177,173, 45,177,173
ColorAssign3="trunk""/trunk.*" 4,58,63, 4,58,63
ColorAssign4="trunk/code_swarm""/trunk/code_swarm.*" 145,33,133, 145,33,133
ColorAssign5="trunk/convert_logs""/trunk/convert_logs.*" 246,240,209, 246,240,209
ColorAssign6="trunk/data""/trunk/data.*" 24,166,21, 24,166,21
ColorAssign7="trunk/dist""/trunk/dist.*" 255,129,130, 255,129,130
ColorAssign8="trunk/eclipse""/trunk/eclipse.*" 211,191,125, 211,191,125
ColorAssign9="trunk/lib""/trunk/lib.*" 245,40,188, 245,40,188
ColorAssign10="trunk/physics_engine""/trunk/physics_engine.*" 128,140,154, 128,140,154
ColorAssign11="trunk/prototype""/trunk/prototype.*" 123,234,36, 123,234,36
ColorAssign12="trunk/src""/trunk/src.*" 216,68,75, 216,68,75
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
    

