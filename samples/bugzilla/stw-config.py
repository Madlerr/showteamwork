
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="Attic", "/cvsroot/mozilla/webtools/bugzilla/Attic.*", 69,182,99, 69,182,99
ColorAssign2="Bugzilla", "/cvsroot/mozilla/webtools/bugzilla/Bugzilla.*", 10,115,20, 10,115,20
ColorAssign3="Bugzilla/DB", "/cvsroot/mozilla/webtools/bugzilla/Bugzilla/DB.*", 243,155,33, 243,155,33
ColorAssign4="docs", "/cvsroot/mozilla/webtools/bugzilla/docs.*", 157,79,118, 157,79,118
ColorAssign5="docs/en", "/cvsroot/mozilla/webtools/bugzilla/docs/en.*", 202,225,154, 202,225,154
ColorAssign6="docs/html", "/cvsroot/mozilla/webtools/bugzilla/docs/html.*", 33,18,171, 33,18,171
ColorAssign7="docs/sgml", "/cvsroot/mozilla/webtools/bugzilla/docs/sgml.*", 244,249,252, 244,249,252
ColorAssign8="docs/xml", "/cvsroot/mozilla/webtools/bugzilla/docs/xml.*", 234,164,203, 234,164,203
ColorAssign9="t", "/cvsroot/mozilla/webtools/bugzilla/t.*", 27,192,208, 27,192,208
ColorAssign10="template", "/cvsroot/mozilla/webtools/bugzilla/template.*", 163,180,48, 163,180,48
ColorAssign11="template/default", "/cvsroot/mozilla/webtools/bugzilla/template/default.*", 20,179,134, 20,179,134
ColorAssign12="template/en", "/cvsroot/mozilla/webtools/bugzilla/template/en.*", 86,3,214, 86,3,214
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
    

