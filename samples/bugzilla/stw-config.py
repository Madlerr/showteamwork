
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""
ColorAssign1="Bugzilla", "/cvsroot/mozilla/webtools/bugzilla/Bugzilla.*|.*\.cgi", 255,0,0,       255,0,0
ColorAssign2="docs",     "/cvsroot/mozilla/webtools/bugzilla/docs.*",     212,183,3,     212,183,3
ColorAssign3="template", "/cvsroot/mozilla/webtools/bugzilla/template.*", 77,175,90,     77,175,90
ColorAssign4="contrib",  "/cvsroot/mozilla/webtools/bugzilla/contrib.*",  10,198,20,     10,198,20
ColorAssign5="skins",    "/cvsroot/mozilla/webtools/bugzilla/skins.*",    201,28,194,    201,28,194
ColorAssign6="Attic",    "/cvsroot/mozilla/webtools/bugzilla/Attic.*",    0,2,216,     0,2,216
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

engine="""
# name of the engine class
name=PhysicsEngineChaotic

# parameters specific to this engine
drag=0.00001
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
Background=0,0,20
    """

GOURCE=1
CODESWARM=1

print config, engine    
    

