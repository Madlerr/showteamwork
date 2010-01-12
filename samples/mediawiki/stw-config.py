
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


ColorAssign1="branches""/branches.*" 30,147,125, 30,147,125
ColorAssign2="branches/ApiEdit_Vodafone""/branches/ApiEdit_Vodafone.*" 213,108,202, 213,108,202
ColorAssign3="branches/liquidthreads""/branches/liquidthreads.*" 13,62,50, 13,62,50
ColorAssign4="branches/new-installer""/branches/new-installer.*" 248,241,187, 248,241,187
ColorAssign5="branches/new-upload""/branches/new-upload.*" 133,212,232, 133,212,232
ColorAssign6="civicrm""/civicrm.*" 166,5,218, 166,5,218
ColorAssign7="civicrm/trunk""/civicrm/trunk.*" 255,220,67, 255,220,67
ColorAssign8="civicrm/vendor""/civicrm/vendor.*" 27,54,227, 27,54,227
ColorAssign9="trunk""/trunk.*" 187,163,169, 187,163,169
ColorAssign10="trunk/debs""/trunk/debs.*" 196,228,11, 196,228,11
ColorAssign11="trunk/extensions""/trunk/extensions.*" 53,104,125, 53,104,125
ColorAssign12="trunk/phase3""/trunk/phase3.*" 122,224,72, 122,224,72
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
    

