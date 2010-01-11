
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


ColorAssign1="branches""/subversion/branches.*" 173,109,183, 173,109,183
ColorAssign2="branches/fsfs-pack""/subversion/branches/fsfs-pack.*" 111,206,245, 111,206,245
ColorAssign3="branches/ignore-mergeinfo""/subversion/branches/ignore-mergeinfo.*" 24,35,149, 24,35,149
ColorAssign4="branches/svnpatch-diff""/subversion/branches/svnpatch-diff.*" 35,142,90, 35,142,90
ColorAssign5="trunk""/subversion/trunk.*" 112,66,31, 112,66,31
ColorAssign6="trunk/build""/subversion/trunk/build.*" 227,251,176, 227,251,176
ColorAssign7="trunk/contrib""/subversion/trunk/contrib.*" 224,235,40, 224,235,40
ColorAssign8="trunk/notes""/subversion/trunk/notes.*" 186,157,105, 186,157,105
ColorAssign9="trunk/packages""/subversion/trunk/packages.*" 78,163,169, 78,163,169
ColorAssign10="trunk/subversion""/subversion/trunk/subversion.*" 76,78,80, 76,78,80
ColorAssign11="trunk/tools""/subversion/trunk/tools.*" 133,209,35, 133,209,35
ColorAssign12="trunk/www""/subversion/trunk/www.*" 159,163,54, 159,163,54
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
    

