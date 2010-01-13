
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="contrib", "contrib.*", 97,17,143, 97,17,143
ColorAssign2="doc", "doc.*", 208,136,67, 208,136,67
ColorAssign3="hgext", "hgext.*", 138,202,218, 138,202,218
ColorAssign4="hgext/convert", "hgext/convert.*", 30,119,85, 30,119,85
ColorAssign5="hgext/inotify", "hgext/inotify.*", 217,227,136, 217,227,136
ColorAssign6="i18n", "i18n.*", 2,199,12, 2,199,12
ColorAssign7="mercurial", "mercurial.*", 251,249,243, 251,249,243
ColorAssign8="mercurial/hgweb", "mercurial/hgweb.*", 21,42,4, 21,42,4
ColorAssign9="templates", "templates.*", 226,121,198, 226,121,198
ColorAssign10="templates/coal", "templates/coal.*", 91,226,135, 91,226,135
ColorAssign11="templates/gitweb", "templates/gitweb.*", 38,93,138, 38,93,138
ColorAssign12="tests", "tests.*", 101,148,208, 101,148,208
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
    

