
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


ColorAssign1="branches""/branches.*" 158,207,24, 158,207,24
ColorAssign2="branches/REL1_14""/branches/REL1_14.*" 4,186,152, 4,186,152
ColorAssign3="branches/REL1_15""/branches/REL1_15.*" 93,56,196, 93,56,196
ColorAssign4="branches/js2-work""/branches/js2-work.*" 193,234,189, 193,234,189
ColorAssign5="branches/new-installer""/branches/new-installer.*" 84,9,73, 84,9,73
ColorAssign6="branches/wmf-deployment""/branches/wmf-deployment.*" 247,250,254, 247,250,254
ColorAssign7="tags""/tags.*" 38,231,19, 38,231,19
ColorAssign8="tags/extensions""/tags/extensions.*" 164,80,86, 164,80,86
ColorAssign9="trunk""/trunk.*" 101,138,133, 101,138,133
ColorAssign10="trunk/extensions""/trunk/extensions.*" 49,73,248, 49,73,248
ColorAssign11="trunk/phase3""/trunk/phase3.*" 3,48,64, 3,48,64
ColorAssign12="trunk/tools""/trunk/tools.*" 66,148,42, 66,148,42
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
    

