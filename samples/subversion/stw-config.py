
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="branches", "/subversion/branches.*", 60,68,138, 60,68,138
ColorAssign2="branches/fsfs-pack", "/subversion/branches/fsfs-pack.*", 60,203,216, 60,203,216
ColorAssign3="branches/ignore-mergeinfo", "/subversion/branches/ignore-mergeinfo.*", 191,216,195, 191,216,195
ColorAssign4="branches/svnpatch-diff", "/subversion/branches/svnpatch-diff.*", 66,156,50, 66,156,50
ColorAssign5="trunk", "/subversion/trunk.*", 7,21,223, 7,21,223
ColorAssign6="trunk/build", "/subversion/trunk/build.*", 253,252,112, 253,252,112
ColorAssign7="trunk/contrib", "/subversion/trunk/contrib.*", 189,42,119, 189,42,119
ColorAssign8="trunk/notes", "/subversion/trunk/notes.*", 154,235,8, 154,235,8
ColorAssign9="trunk/packages", "/subversion/trunk/packages.*", 196,221,200, 196,221,200
ColorAssign10="trunk/subversion", "/subversion/trunk/subversion.*", 151,182,147, 151,182,147
ColorAssign11="trunk/tools", "/subversion/trunk/tools.*", 97,70,165, 97,70,165
ColorAssign12="trunk/www", "/subversion/trunk/www.*", 33,162,81, 33,162,81
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
CODESWARM=0

print config, engine    
    

