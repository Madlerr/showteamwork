
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""


ColorAssign1="audio", "audio.*", 249,250,254, 249,250,254
ColorAssign2="samples/bugzilla", "samples/bugzilla.*", 238,232,152, 238,232,152
ColorAssign3="samples/bzr-svn", "samples/bzr-svn.*", 181,226,197, 181,226,197
ColorAssign4="samples/ffmpeg", "samples/ffmpeg.*", 170,235,25, 170,235,25
ColorAssign5="samples/postgres", "samples/postgres.*", 132,167,220, 132,167,220
ColorAssign6="samples/viewvc-last", "samples/viewvc-last.*", 118,172,220, 118,172,220
ColorAssign7="samples", "samples.*", 55,178,157, 55,178,157
ColorAssign8="src", "src.*", 158,127,129, 158,127,129
ColorAssign9="tools/data", "tools/data.*", 230,36,185, 230,36,185
ColorAssign10="tools/lib", "tools/lib.*", 132,102,59, 132,102,59
ColorAssign11="tools/nt", "tools/nt.*", 76,47,232, 76,47,232
ColorAssign12="tools", "tools.*", 106,1,69, 106,1,69
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
    

