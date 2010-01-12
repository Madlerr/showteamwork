
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


ColorAssign1="contrib""contrib.*" 197,48,102, 197,48,102
ColorAssign2="doc""doc.*" 167,209,158, 167,209,158
ColorAssign3="hgext""hgext.*" 26,199,240, 26,199,240
ColorAssign4="hgext/convert""hgext/convert.*" 59,24,191, 59,24,191
ColorAssign5="hgext/inotify""hgext/inotify.*" 243,255,25, 243,255,25
ColorAssign6="i18n""i18n.*" 253,255,252, 253,255,252
ColorAssign7="mercurial""mercurial.*" 153,134,7, 153,134,7
ColorAssign8="mercurial/hgweb""mercurial/hgweb.*" 114,62,60, 114,62,60
ColorAssign9="templates""templates.*" 46,232,52, 46,232,52
ColorAssign10="templates/coal""templates/coal.*" 138,86,149, 138,86,149
ColorAssign11="templates/gitweb""templates/gitweb.*" 54,237,64, 54,237,64
ColorAssign12="tests""tests.*" 70,174,109, 70,174,109
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
    

