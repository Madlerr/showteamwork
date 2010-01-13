
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="branches", "/branches.*", 37,86,219, 37,86,219
ColorAssign2="branches/ApiEdit_Vodafone", "/branches/ApiEdit_Vodafone.*", 136,204,52, 136,204,52
ColorAssign3="branches/liquidthreads", "/branches/liquidthreads.*", 49,3,129, 49,3,129
ColorAssign4="branches/new-installer", "/branches/new-installer.*", 226,69,62, 226,69,62
ColorAssign5="branches/new-upload", "/branches/new-upload.*", 228,213,115, 228,213,115
ColorAssign6="civicrm", "/civicrm.*", 225,239,253, 225,239,253
ColorAssign7="civicrm/trunk", "/civicrm/trunk.*", 104,43,8, 104,43,8
ColorAssign8="civicrm/vendor", "/civicrm/vendor.*", 53,195,101, 53,195,101
ColorAssign9="trunk", "/trunk.*", 198,41,233, 198,41,233
ColorAssign10="trunk/debs", "/trunk/debs.*", 21,86,110, 21,86,110
ColorAssign11="trunk/extensions", "/trunk/extensions.*", 138,114,246, 138,114,246
ColorAssign12="trunk/phase3", "/trunk/phase3.*", 56,237,120, 56,237,120
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
    

