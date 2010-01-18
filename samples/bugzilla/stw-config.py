
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="Attic", "/cvsroot/mozilla/webtools/bugzilla/Attic.*", 215,242,146, 215,242,146
ColorAssign2="Bugzilla", "/cvsroot/mozilla/webtools/bugzilla/Bugzilla.*", 207,240,62, 207,240,62
ColorAssign3="docs", "/cvsroot/mozilla/webtools/bugzilla/docs.*", 198,152,247, 198,152,247
ColorAssign4="docs/html", "/cvsroot/mozilla/webtools/bugzilla/docs/html.*", 172,143,250, 172,143,250
ColorAssign5="docs/xml", "/cvsroot/mozilla/webtools/bugzilla/docs/xml.*", 155,131,184, 155,131,184
ColorAssign6="template", "/cvsroot/mozilla/webtools/bugzilla/template.*", 6,195,37, 6,195,37
ColorAssign7="template/en/default", "/cvsroot/mozilla/webtools/bugzilla/template/en/default.*", 132,120,49, 132,120,49
ColorAssign8="template/en/default/admin", "/cvsroot/mozilla/webtools/bugzilla/template/en/default/admin.*", 9,115,81, 9,115,81
ColorAssign9="template/en/default/bug", "/cvsroot/mozilla/webtools/bugzilla/template/en/default/bug.*", 75,21,104, 75,21,104
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
    

