
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="/debs", "/trunk/debs.*", 241,238,126, 241,238,126
ColorAssign2="/extensions/FlaggedRevs", "/trunk/extensions/FlaggedRevs.*", 150,236,108, 150,236,108
ColorAssign3="/extensions/MetavidWiki", "/trunk/extensions/MetavidWiki.*", 194,223,38, 194,223,38
ColorAssign4="/extensions/SemanticMediaWiki", "/trunk/extensions/SemanticMediaWiki.*", 86,206,123, 86,206,123
ColorAssign5="/extensions/UsabilityInitiative", "/trunk/extensions/UsabilityInitiative.*", 162,92,167, 162,92,167
ColorAssign6="/phase3/includes", "/trunk/phase3/includes.*", 179,15,232, 179,15,232
ColorAssign7="/phase3/languages/messages", "/trunk/phase3/languages/messages.*", 43,63,19, 43,63,19
ColorAssign8="/phase3/languages", "/trunk/phase3/languages.*", 134,12,7, 134,12,7
ColorAssign9="/", "/trunk.*", 31,11,163, 31,11,163
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
    

