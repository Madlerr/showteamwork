
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


ColorAssign1="contrib""/pgsql/contrib.*" 243,128,184, 243,128,184
ColorAssign2="doc""/pgsql/doc.*" 80,143,173, 80,143,173
ColorAssign3="doc/Attic""/pgsql/doc/Attic.*" 103,19,226, 103,19,226
ColorAssign4="doc/src""/pgsql/doc/src.*" 170,229,254, 170,229,254
ColorAssign5="src""/pgsql/src.*" 33,41,33, 33,41,33
ColorAssign6="src/backend""/pgsql/src/backend.*" 193,53,77, 193,53,77
ColorAssign7="src/bin""/pgsql/src/bin.*" 254,253,164, 254,253,164
ColorAssign8="src/include""/pgsql/src/include.*" 118,238,141, 118,238,141
ColorAssign9="src/interfaces""/pgsql/src/interfaces.*" 240,49,45, 240,49,45
ColorAssign10="src/pl""/pgsql/src/pl.*" 128,81,91, 128,81,91
ColorAssign11="src/test""/pgsql/src/test.*" 81,37,28, 81,37,28
ColorAssign12="src/tools""/pgsql/src/tools.*" 215,41,183, 215,41,183
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
    

