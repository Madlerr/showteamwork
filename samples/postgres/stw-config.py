
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="contrib", "/pgsql/contrib.*", 67,132,17, 67,132,17
ColorAssign2="doc", "/pgsql/doc.*", 43,249,241, 43,249,241
ColorAssign3="doc/Attic", "/pgsql/doc/Attic.*", 144,168,136, 144,168,136
ColorAssign4="doc/src", "/pgsql/doc/src.*", 109,13,25, 109,13,25
ColorAssign5="src", "/pgsql/src.*", 230,242,140, 230,242,140
ColorAssign6="src/backend", "/pgsql/src/backend.*", 220,96,59, 220,96,59
ColorAssign7="src/bin", "/pgsql/src/bin.*", 237,1,2, 237,1,2
ColorAssign8="src/include", "/pgsql/src/include.*", 253,251,254, 253,251,254
ColorAssign9="src/interfaces", "/pgsql/src/interfaces.*", 232,225,60, 232,225,60
ColorAssign10="src/pl", "/pgsql/src/pl.*", 201,249,165, 201,249,165
ColorAssign11="src/test", "/pgsql/src/test.*", 68,235,98, 68,235,98
ColorAssign12="src/tools", "/pgsql/src/tools.*", 221,90,30, 221,90,30
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
    

