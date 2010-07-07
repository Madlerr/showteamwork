
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="Documentation", "Documentation.*", 253,255,251, 253,255,251
ColorAssign2="compat", "compat.*", 251,230,149, 251,230,149
ColorAssign3="contrib", "contrib.*", 113,247,238, 113,247,238
ColorAssign4="contrib/completion", "contrib/completion.*", 200,170,211, 200,170,211
ColorAssign5="contrib/fast-import", "contrib/fast-import.*", 97,211,197, 97,211,197
ColorAssign6="contrib/git-svn", "contrib/git-svn.*", 236,116,88, 236,116,88
ColorAssign7="gitweb", "gitweb.*", 21,141,230, 21,141,230
ColorAssign8="lib", "lib.*", 63,101,230, 63,101,230
ColorAssign9="po", "po.*", 149,26,192, 149,26,192
ColorAssign10="t", "t.*", 131,19,213, 131,19,213
ColorAssign11="t/t4013", "t/t4013.*", 116,14,77, 116,14,77
ColorAssign12="t/t5515", "t/t5515.*", 17,53,83, 17,53,83
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
    

