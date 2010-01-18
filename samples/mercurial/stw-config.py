
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="contrib", "contrib.*", 249,249,225, 249,249,225
ColorAssign2="doc", "doc.*", 242,232,80, 242,232,80
ColorAssign3="hgext", "hgext.*", 180,215,135, 180,215,135
ColorAssign4="hgext/convert", "hgext/convert.*", 174,206,3, 174,206,3
ColorAssign5="hgext/inotify", "hgext/inotify.*", 118,192,219, 118,192,219
ColorAssign6="i18n", "i18n.*", 168,127,244, 168,127,244
ColorAssign7="mercurial", "mercurial.*", 159,104,247, 159,104,247
ColorAssign8="mercurial/hgweb", "mercurial/hgweb.*", 237,77,164, 237,77,164
ColorAssign9="templates", "templates.*", 13,156,49, 13,156,49
ColorAssign10="templates/coal", "templates/coal.*", 127,52,39, 127,52,39
ColorAssign11="templates/gitweb", "templates/gitweb.*", 165,10,41, 165,10,41
ColorAssign12="tests", "tests.*", 56,1,150, 56,1,150
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
    

