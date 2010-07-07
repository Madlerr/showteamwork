
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="/extensions/FlaggedRevs/language", "/trunk/extensions/FlaggedRevs/language.*", 250,254,187, 250,254,187
ColorAssign2="/extensions/FlaggedRevs", "/trunk/extensions/FlaggedRevs.*", 133,241,253, 133,241,253
ColorAssign3="/extensions/Maps", "/trunk/extensions/Maps.*", 204,193,226, 204,193,226
ColorAssign4="/extensions/Storyboard", "/trunk/extensions/Storyboard.*", 160,181,146, 160,181,146
ColorAssign5="/extensions/UsabilityInitiative", "/trunk/extensions/UsabilityInitiative.*", 11,231,51, 11,231,51
ColorAssign6="/phase3/includes", "/trunk/phase3/includes.*", 200,117,52, 200,117,52
ColorAssign7="/phase3/languages/messages", "/trunk/phase3/languages/messages.*", 232,44,200, 232,44,200
ColorAssign8="/phase3/languages", "/trunk/phase3/languages.*", 69,76,71, 69,76,71
ColorAssign9="/WikiWord", "/trunk/WikiWord.*", 6,39,96, 6,39,96
ColorAssign10="/", "/trunk.*", 1,26,145, 1,26,145
"""

#Below you need to set variables «config» and «engine» (needed for CodeSwarm only)

engine="""
# name of the engine class
name=PhysicsEngineSimple

# parameters specific to this engine
edgeMultiplier=1.0
speedMultiplier=1.0
nodesMultiplier=1.0
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
    

