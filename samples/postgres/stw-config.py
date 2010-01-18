
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="contrib", "/pgsql/contrib.*", 255,254,202, 255,254,202
ColorAssign2="doc", "/pgsql/doc.*", 213,244,33, 213,244,33
ColorAssign3="doc/src", "/pgsql/doc/src.*", 156,183,106, 156,183,106
ColorAssign4="src", "/pgsql/src.*", 106,119,238, 106,119,238
ColorAssign5="src/backend", "/pgsql/src/backend.*", 211,25,170, 211,25,170
ColorAssign6="src/bin", "/pgsql/src/bin.*", 155,86,3, 155,86,3
ColorAssign7="src/include", "/pgsql/src/include.*", 209,3,223, 209,3,223
ColorAssign8="src/interfaces", "/pgsql/src/interfaces.*", 77,89,14, 77,89,14
ColorAssign9="src/test", "/pgsql/src/test.*", 40,14,128, 40,14,128
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
    

