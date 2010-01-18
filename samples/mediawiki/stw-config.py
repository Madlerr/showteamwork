
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="branches", "/branches.*", 252,243,241, 252,243,241
ColorAssign2="civicrm", "/civicrm.*", 185,229,195, 185,229,195
ColorAssign3="civicrm/trunk/sites", "/civicrm/trunk/sites.*", 241,194,129, 241,194,129
ColorAssign4="civicrm/trunk/sites/all", "/civicrm/trunk/sites/all.*", 84,217,181, 84,217,181
ColorAssign5="civicrm/trunk/sites/all/modules", "/civicrm/trunk/sites/all/modules.*", 82,214,100, 82,214,100
ColorAssign6="civicrm/trunk/sites/all/modules/civicrm", "/civicrm/trunk/sites/all/modules/civicrm.*", 227,58,203, 227,58,203
ColorAssign7="trunk", "/trunk.*", 236,15,89, 236,15,89
ColorAssign8="trunk/extensions", "/trunk/extensions.*", 18,93,212, 18,93,212
ColorAssign9="trunk/phase3/languages", "/trunk/phase3/languages.*", 160,1,41, 160,1,41
ColorAssign10="trunk/phase3/languages/messages", "/trunk/phase3/languages/messages.*", 70,9,132, 70,9,132
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
    

