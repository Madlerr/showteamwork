
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


ColorAssign1="Attic""/cvsroot/mozilla/webtools/bugzilla/Attic.*" 96,196,125, 96,196,125
ColorAssign2="Bugzilla""/cvsroot/mozilla/webtools/bugzilla/Bugzilla.*" 157,34,128, 157,34,128
ColorAssign3="Bugzilla/DB""/cvsroot/mozilla/webtools/bugzilla/Bugzilla/DB.*" 252,187,81, 252,187,81
ColorAssign4="docs""/cvsroot/mozilla/webtools/bugzilla/docs.*" 124,105,240, 124,105,240
ColorAssign5="docs/en""/cvsroot/mozilla/webtools/bugzilla/docs/en.*" 225,250,225, 225,250,225
ColorAssign6="docs/html""/cvsroot/mozilla/webtools/bugzilla/docs/html.*" 4,53,15, 4,53,15
ColorAssign7="docs/sgml""/cvsroot/mozilla/webtools/bugzilla/docs/sgml.*" 85,41,74, 85,41,74
ColorAssign8="docs/xml""/cvsroot/mozilla/webtools/bugzilla/docs/xml.*" 217,251,48, 217,251,48
ColorAssign9="t""/cvsroot/mozilla/webtools/bugzilla/t.*" 33,141,166, 33,141,166
ColorAssign10="template""/cvsroot/mozilla/webtools/bugzilla/template.*" 44,138,106, 44,138,106
ColorAssign11="template/default""/cvsroot/mozilla/webtools/bugzilla/template/default.*" 166,57,26, 166,57,26
ColorAssign12="template/en""/cvsroot/mozilla/webtools/bugzilla/template/en.*" 82,45,120, 82,45,120
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
    

