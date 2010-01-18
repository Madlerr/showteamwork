#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  All high-level processing of VCS log visualization.
"""
import sys
import os
import time
import re
import heapq
import operator
import tempfile
import shutil
import math
import random
from ColorPalette       import RandomColorPalette
from EventList          import EventList
from RingBuffer         import RingBuffer
from STWUtils           import *

  
class VCSVisualizer:
    """
       Automatic building of VCS-logs visualization using Codeswarm and Gource engines.
       Only one necessary file: «[VCS].log» and «audio.mp3»
          
       Also you can customize
       «stw-scenario.txt», «stw-audio.mp3», «stw-config.py»
       
       Measuring of audiofile «stw-audio.mp3» length and various metrics of input «activity.xml» file.
       Can generate template of script scenario file and template of coloring most used directories.
    """
    version__ = "$Id4$"
    
    def __init__(self, inputfile):
        """
           Check for input files,
           substitute random defaults for missing audio files.
        """
        self.toolsdir = os.path.realpath(
                        os.path.join(os.path.dirname(sys.argv[0]),
                                       "../tools"))
        
        if os.name == "nt":
            self.exedir = os.path.realpath(os.path.join(self.toolsdir, os.name ))
        else:
            # Under Linux you have to [build and] install ffmpeg, mencoder, gource to PATH 
            self.exedir = ''

        self.fontpath = os.path.realpath(os.path.join(self.toolsdir,
                                                      "/".join(["fonts","FreeSans.ttf"])))

        #home/working directory 
        self.homedir = os.getcwd()
        
        self.inputfile = os.path.realpath(os.path.join(self.homedir, inputfile))
        self.projectdir, self.filename = os.path.split(self.inputfile)
        l = self.projectdir.split(os.path.sep)
        self.projectname = l[-1]
        if len(l) > 1 and l[-1] in ["trunk", "tags", "branches"]:
            self.projectname = "-".join( l[-2:] )    
        self.tempdir = tempfile.gettempdir()
        self.inputhash = hash4file(inputfile)
        
        self.audiopath = os.path.join(self.projectdir, "stw-audio.mp3")
        if not file_is_ok(self.audiopath):
            audiodir = os.path.realpath(os.path.join(self.toolsdir, "../audio"))
            audiolist = os.listdir(audiodir)
            mp3list = [s for s in audiolist if os.path.splitext(s)[1] == ".mp3"]
            if  len(mp3list) == 0:
                raise Exception("""
<stw-audio.mp3> is missing and no default MP3 files in <audio> folder.
Please, provide audio track for your clip.
""")
            audio = random.choice(mp3list)
            shutil.copy(os.path.join(audiodir, audio), self.audiopath)
            
        self.audiohash = hash4file(self.audiopath)
        s = "STW-%(projectname)s-%(inputhash)s-%(audiohash)s" % vars(self)
        self.workdir = os.path.join(self.tempdir, s)
        createdir(self.workdir)
        
        self.need_gource = 1
        self.need_codeswarm = 1
        
        
    def get_movie_length(self, filepath):
        """
        Measure length of audio or movie file using ``ffmpeg``.
        """
        scmd = r'%s\ffmpeg -i %s' % (self.exedir, filepath)
        progin, progout = os.popen4(scmd)
        mp3info = progout.read()
        progin.close()
        progout.close()
        
        reg = re.compile(
            r"(?sm)Duration: (?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d.?\d?\d?),"
                        )
        m = reg.search(mp3info)
        if m:    
            hours = int(m.group("hours"))
            minutes = int(m.group("minutes"))
            seconds = float(m.group("seconds"))
            movielength = hours*3600+minutes*60+seconds
            return movielength
        else:   
            raise Exception("Can not determine duration of <%s>" % filepath) 
    
    
    def analyze_events(self, elist):
        """
          Get comments for «scenario template»,
          count statistics for filepath,
          make default coloring rules for Codeswarm
        """
        self.startdate = time.strptime("01.01.2049", "%d.%m.%Y")
        self.enddate   = time.localtime(0)
        
        template = ""        
        commentline = None
        authors = {}
        rating = {}
        paths = []
        
        for event in elist.events:
            paths.append(event.filename)
        commonprefix = os.path.commonprefix(paths)    
            
        for event in elist.events:
            reducedpath = event.filename[len(commonprefix):]
            reducedpath = reducedpath.replace("\\","/")
            path = reducedpath.split("/")
            for i in xrange(1, len(path)):
                code = "/".join(path[:i])
                if code != reducedpath and code != "":    
                    if code not in rating:
                        rating[code] = 0
                    rating[code] += 1

            vcstime = time.localtime(float(event.date)/1000)
            if vcstime < self.startdate:
                self.startdate = vcstime
            if vcstime > self.enddate:
                self.enddate = vcstime
            dates = time.strftime("%Y-%m-%d", vcstime)

            prevcommentline = commentline

            if event.author not in authors:
                template += "".join(["\n", dates, ' Hi ', event.author, '!'])
                authors[event.author] = dates
            
            if len(event.comment)>0:
                commentline = event.author + ": " + event.comment[:64]             
                if commentline != prevcommentline:    
                    template += "".join(["\n#", dates, ' ', commentline])
                
        self.historylength = time.mktime(self.enddate) - time.mktime(self.startdate)
        self.template = template
        toppath = heapq.nlargest(12, rating.iteritems(), operator.itemgetter(1))
        cluster = {}
        for it in toppath:
            code = "/".join(it[0].split("/")[:2])
            if code not in cluster:
                cluster[code] = []
            cluster[code].append(it[0])
            
        paths = []    
        for k, v in cluster.iteritems():
            if len(v)<3:
                paths.append(k) 
            else:
                for p in v:
                    if p != k:
                        paths.append(p)     
        
        self.toppaths = paths
        self.toppaths.sort()
        self.commonprefix = commonprefix
    
    def write_default_config(self):
        """
          Write default config with autogenerated coloring template.
        """
        rcp = RandomColorPalette(
                    num = len(self.toppaths),
                    contrast_colors_num = len(self.toppaths)-1
                                )
        
        ls = ""
        
        commonprefix2 = os.path.commonprefix(self.toppaths)
        if commonprefix2 != "":
            self.commonprefix += commonprefix2
            for i,p in enumerate(self.toppaths):
                self.toppaths[i] = p[len(commonprefix2):]
        
        for i, c in enumerate(rcp.colors):
            ix = i + 1
            path = self.toppaths[i]
#            if path != "":
            ls += "".join([
                    '\nColorAssign', str(ix), '="', path, '", ',
                    '"', self.commonprefix, path, '.*", ', str(c), ', ', str(c) ])

        lf = open(self.configpath, "w")
        lf.write(
'''
# -*- coding: utf-8 -*-
# Color assignment rules
# Keep in order, do not skip numbers. Numbers start at 1.
# 
# Pattern:  "Label", "regex", R,G,B, R,G,B
# Label is optional.  If it is omitted, the regex will be used.
#
config="""

%s
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
    

''' %  ls.encode("utf-8"))
        lf.close()
    
    
    def process_user_config(self):
        """
           Process simple user config and
           get codeswarm config and gource config
        """
        self.cswd = os.path.realpath(os.path.join(self.toolsdir, "..")
                                     ).replace("\\","/")
        self.cwsnapshotdir = os.path.join(self.workdir, self.confighash)
        createdir(self.cwsnapshotdir)
 
        localvars = {}
        execfile(self.configpath, localvars)
        
        usrcfg = ""
        if "config" in localvars:
            usrcfg = localvars["config"]

            usrcfg += "".join(["\n", "InputFile=", self.activitypath, "\n"])

        if "engine" in localvars:
            for engine in [
                           "PhysicsEngineSimple",
                           "PhysicsEngineChaotic",
                           "PhysicsEngineLegacy",
                           "PhysicsEngineMaxwellsDemon"
                           ]:
                re_ = r"(?m)^name="+engine+r"\s+" 
                if re.compile(re_).search(localvars["engine"]):
                    codeswarmenginefile = os.path.join(self.workdir, engine + ".config")
                    lf = open(codeswarmenginefile, "w")
                    lf.write(localvars["engine"])
                    lf.close()
                    usrcfg += "".join([
        'PhysicsEngineConfigDir=', self.workdir, '\n',
        'PhysicsEngineSelection=', engine, '\n'])
                    break

        usrcfg = usrcfg.replace("\\","/")
        self.config = """
GOURCE=1
CODESWARM=1
Height=800
InputFile=%(workdir)s/activity.xml
PhysicsEngineConfigDir=%(cswd)s/tools/codeswarm_physics_engine
ParticleSpriteFile=%(cswd)s/tools/particle.png
Font=DejaVu SansSerif
FontSize=20
BoldFontSize=24
MillisecondsPerFrame=%(ms4frame)s
MaxThreads=4
Background=0,0,0
TakeSnapshots=true
SnapshotLocation=%(cwsnapshotdir)s/cs-#####.png
DrawNamesSharp=true
DrawNamesHalos=true
DrawFilesSharp=false
DrawFilesFuzzy=true
DrawFilesJelly=true
ShowLegend=true
ShowHistory=true
ShowDate=true
ShowEdges=true
ShowDebug=false
EdgeLength=25
EdgeDecrement=-2
FileDecrement=-2
PersonDecrement=-1
FileSpeed=7.0
PersonSpeed=2.0
FileMass=1.0
PersonMass=4.0
EdgeLife=250
FileLife=200
PersonLife=255
HighlightPct=5
PhysicsEngineSelection=PhysicsEngineSimple
UseOpenGL=false
        """ % vars(self)
        self.config = self.config.replace("\\","/")

        for line in self.config.split("\n"):
            if line.find("=")>0:
                option, value = line.split("=")
                option = option.strip()
                value = value.strip()
                if usrcfg.lower().find("\n%s=" % option.lower()) < 0:
                    usrcfg += "\n\n%s=%s\n" % (option, value)


        if "GOURCE" in localvars:
            self.need_gource = localvars["GOURCE"]    
        if "CODESWARM" in localvars:
            self.need_codeswarm = localvars["CODESWARM"]    

        usrcfg = re.sub(r"(?sm)\s+\n", "\n", usrcfg)
        usrcfg = re.sub(r"(?sm)(CODESWARM|GOURCE)=([\d]+)\s*\n", "", usrcfg)



        lf = open(self.configobjpath, "w")
        lf.write(usrcfg.encode("utf-8"))
        lf.close()
        
        background_re = re.compile(r"(?sm)Background=(?P<R>[\d]+),(?P<G>[\d]+),(?P<B>[\d]+)\s+\n")
        m = background_re.search(usrcfg)
        self.background = "000000"
        if m:
            self.background = "%02x%02x%02x" % (
                                int(m.group("R")), int(m.group("G")), int(m.group("B")))

        self.width = getintparam(usrcfg, "Width", 640)
        self.height = getintparam(usrcfg, "Height", 640)


    def process_subtitles(self, srtpath):
        '''
        Process ``scenario.txt``,
        translate «date-based» subtitles to time-bases SRT-subtitles.
        '''
        lf = open(self.scenariopath, "r")
        subtitles = lf.read().decode("utf-8")
        lf.close()
    
        subtitles = re.sub(r"(?m)^#[^\n]*\n?", "", subtitles)
        scenario = []
        for line in subtitles.splitlines():
            if len(line.strip())>1:
                datas, text = line.split(" ", 1)
                vcstime = None
                datas = datas.replace(u'\ufeff','')
                for format in ["%d.%m.%Y", "%Y-%m-%d"]:
                    try:
                        vcstime = time.strptime(datas.encode("latin-1"), format)
                        break
                    except ValueError:
                        pass
                if not vcstime:
                    print "Warning: can not understand date <%s>" % datas

                subtitletimestart = (time.mktime(vcstime) -
                    time.mktime(self.startdate)) * self.movielength / self.historylength
                if -1 < subtitletimestart < 0:
                    subtitletimestart = 0
                if subtitletimestart < 0:
                    print "Date <%s> before start of work history" % datas
                else:    
                    scenario.append( (subtitletimestart, text) )    

        if len(scenario) == 0:
            return
        
        scenario.sort()
        
        messages = RingBuffer(3)

        class SRTText:
            """
              Subtitles in SRT format
            """
            def __init__(self):
                self.srt = ""
                self.index = 0
                self.stime = float(max([scenario[0][0]-1, 0]))
                self.etime = 0.0
            
            def append(self, messages):
                """
                Append subtitle from list of messages
                """
                ml = messages.get()
                msg = " * ".join(ml)
                subtitletimestart_str = time.strftime("%H:%M:%S", time.gmtime(self.stime))
                subtitletimeend_str = time.strftime("%H:%M:%S", time.gmtime(self.etime))
                self.srt += """
%d
%s,000 --> %s,000
%s
                """ % (self.index, subtitletimestart_str, subtitletimeend_str, msg)    
                self.stime = self.etime
                self.index += 1
                
                
        default_subtitle_time = 3        
        srt_text = SRTText()        
        for s in scenario:
            newtime = float(s[0])
            if newtime > srt_text.stime + default_subtitle_time:
                srt_text.etime = srt_text.stime + default_subtitle_time 
                srt_text.append(messages)
                messages = RingBuffer(3)
                srt_text.stime = newtime
            else:    
                srt_text.etime = newtime
                srt_text.append(messages)
            messages.append(s[1])
        srt_text.etime = min(srt_text.etime + 3, self.movielength)
        srt_text.append(messages)

        lf = open(srtpath, "w")
        lf.write(srt_text.srt.encode("utf-8"))
        lf.close()
    
    
    def process(self):
        """
        Main process. Do all works by «lazy way» — build the only objects,
        that is not already exists (Nano-«SCons/make»). 
        """
        filtereventspath = os.path.join(self.projectdir,"stw-filter-events.py")
        if not file_is_ok(filtereventspath):
            lf = open(filtereventspath, "w")
            lf.write(r"""# -*- coding: utf-8 -*-
import re
import time

def filter_events(event):
    # You can modify event attribute, or disable (filter) event, returning False
    # Sample processing below
    emailre_ = re.compile(r"(?P<email>[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6})",
                    re.IGNORECASE)

    if event.date > time.time()*1000:
       return False # Something wrong — event from future
    
    event.author = event.author.replace('OFFICE\\', '')
    event.author = event.author.lower().replace('"',"'")
    m = emailre_.search(event.author)
    if m:
        event.author = m.group('email') 
    event.author = event.author.replace('"',"'")
    if event.author in ["(no author)"]:
        event.author = "anonymous"
    
    event.comment = re.sub('[Bb][Uu][Gg]\s*\d+\.?', '', event.comment)
    if event.comment.startswith("*** empty log message ***"):
        event.comment = ""

    if len(event.comment) < 10:
        event.comment = ""

    #
    #crap_prefixes=[
    #    "/Users/dumb/myproject/cvs_root/",
    #    "/home/projects/myproject/cvsroot/"
    #]

    #for p in crap_prefixes:
    #    if event.filename.startswith(p):
    #       event.filename=event.filename.replace(p,"/") 

    #event.action=event.action
    return True
""")
            lf.close()

        hash_filter = hash4file(filtereventspath)

        self.activitypath = os.path.join(self.workdir,
                                         "".join(["activity-", hash_filter, ".xml"]))
        activitygourcepath  = os.path.join(self.workdir,
                                         "".join(["activity-", hash_filter, ".gource"]))
        
        events = EventList()    
        if not file_is_ok(self.activitypath) or not file_is_ok(activitygourcepath):
            localvars = {}
            try:
                execfile(filtereventspath, localvars)
            except:
                pass
            if "filter_events" in localvars:
                events.filter_events = localvars["filter_events"]
            else:
                print "Warning: can not load filter for events."
            events.read_log(self.inputfile) 
            events.write_xml(self.activitypath)
            events.write_gource_custom(activitygourcepath)
        else:    
            events.read_log(self.activitypath)
            
        self.movielength = self.get_movie_length(self.audiopath)

        self.analyze_events(events)
        self.ms4frame = int(float(self.historylength*1000)/(self.movielength*24)) - 1
        self.secs4day = float(self.movielength*24*3600)/self.historylength/math.pi

        self.scenariopath = os.path.join(self.projectdir, "stw-scenario.txt")
        if not file_is_ok(self.scenariopath):
            lf = open(self.scenariopath, "w")
        else:    
            lf = open(self.scenariopath + ".template", "w")
        lf.write(self.template.encode("utf-8"))
        lf.close()
        
        self.scenariohash = hash4file(self.scenariopath, self.version__)

        self.configpath = os.path.join(self.projectdir, "stw-config.py")
        self.configobjpath = os.path.join(self.workdir, "stw-config.txt")
        if not file_is_ok(self.configpath):
            self.write_default_config()
            
        self.confighash = hash4file(self.configpath, self.version__)
        self.process_user_config()

        if self.need_codeswarm:
            if not file_is_ok(os.path.join(self.cwsnapshotdir, "cs-00007.png")):
                s = "".join([ 'java -Xmx1000m -classpath ',
                             self.toolsdir, '/code_swarm.jar;',
                             self.toolsdir, '/lib/core.jar;',
                             self.toolsdir, '/lib/xml.jar;',
                             self.toolsdir, '/lib/vecmath.jar;. ',
                             'code_swarm ', self.configobjpath, '/' ])
                print s
                os.system(s)

        gourceconfhash = hash4file(None, "".join([self.exedir, r'\gource',
                     ' -', str(self.width), 'x', str(self.height),
                     ' --background ', self.background,
                     ' --seconds-per-day ', str(self.secs4day),
                     ]) )
        
        grsnapshotdir = os.path.join(self.workdir, "g-"+gourceconfhash)
        createdir(grsnapshotdir)
        gourcerawpath = os.path.join(grsnapshotdir, "gource-raw.avi")
        if not file_is_ok(gourcerawpath):
            s = "".join([self.exedir, r'\gource',
                         ' -', str(self.width), 'x', str(self.height),
                         ' --user-scale 2 --output-framerate 25 ',
                         ' --background ', self.background,
                         ' --stop-position 1 ',
                         ' --highlight-all-users ',
                         r' --date-format "%Y-%m-%d"',
                         ' --seconds-per-day ', str(self.secs4day),
                         ' --log-format custom ',
                         ' --output-ppm-stream ', gourcerawpath, '.ppm ',
                         activitygourcepath ])
            print s
            os.system(s)
            #PPM-file is very Huge. We need to compress it to h264-avi, and kill it.
            s = "".join([self.exedir, r'\ffmpeg',
                         ' -y -b 9000K -f image2pipe -vcodec ppm ',
                         ' -i ', gourcerawpath, '.ppm',
                         ' -vcodec libx264 ', gourcerawpath ])
            print s
            os.system(s)
            os.unlink(gourcerawpath + ".ppm")
            
        srtpath = os.path.join(self.workdir, "".join(["movie-", self.scenariohash, ".srt"]))
        if not file_is_ok(srtpath):
            self.process_subtitles(srtpath)
        
        if self.need_codeswarm:
            moviedir = os.path.join(self.cwsnapshotdir, self.scenariohash)
            createdir(moviedir)
            codeswarmpath = os.path.join(moviedir, "codeswarm.avi")
            if not file_is_ok(codeswarmpath):
                os.chdir(self.cwsnapshotdir)
                framescount = len(os.listdir(self.cwsnapshotdir))
                codeswarmfps = framescount / self.movielength
                s = "".join([ self.exedir, r'\mencoder ',
                             ' mf://*.png -mf ',
                             ' fps=', str(codeswarmfps), ':type=png',
                             ' -ovc x264 -x264encopts pass=1:bitrate=10000 ',
                             ' -oac copy ',
                             ' -audiofile ', self.audiopath,
                             ' -sub ', srtpath,
                             ' -utf8 -font "', self.fontpath, '"',
                             ' -subfont-text-scale 3 -sub-bg-color 20 -sub-bg-alpha 70 ',
                             ' -o ', codeswarmpath ])
                print s
                os.system(s)
                os.chdir(self.homedir)

        if self.need_gource:
            moviedir = os.path.join(grsnapshotdir, self.scenariohash)
            createdir(moviedir)
            gourcepath = os.path.join(moviedir, "gource.avi")
            if not file_is_ok(gourcepath):
                gourcerawlenght = self.get_movie_length(gourcerawpath)
                gourcefps = float(gourcerawlenght / self.movielength)
                os.chdir(self.cwsnapshotdir)
                if not file_is_ok(gourcerawpath + ".fps"):
                    s = "".join([self.exedir, r'\mencoder ', gourcerawpath,
                               ' -ovc x264 -x264encopts pass=1:bitrate=10000 ',
                               ' -ofps 25 -speed ' , str(gourcefps),
                               ' -o ', gourcerawpath, '.fps' ])
                    print s
                    os.system(s)
                s = "".join([self.exedir, r'\mencoder ',
                             gourcerawpath,'.fps',
                             ' -ovc x264 -x264encopts pass=1:bitrate=10000 ',
                             ' -oac copy -audiofile ', self.audiopath,
                             ' -sub ', srtpath,
                             ' -utf8 -font "', self.fontpath, '"',
                             ' -subfont-text-scale 3 ',
                             ' -sub-bg-color 20 -sub-bg-alpha 70 ',
                             ' -o ', gourcepath ])
                print s
                os.system(s)
                os.chdir(self.homedir)
            
        def get_result_path(sourcefile, suffix):
            """
              Get path to result video file, using
              @sourcefile and @suffix
            """
            hash_ = hash4file(sourcefile)
            res = os.path.join(self.projectdir,
                  "".join([self.projectname,"-", suffix, "-", hash_, ".avi"]))
            return res

            
        if self.need_codeswarm:
            resultcodeswarmpath = get_result_path(codeswarmpath, "codeswarm")
            if not file_is_ok(resultcodeswarmpath):
                shutil.copy(codeswarmpath, resultcodeswarmpath)
        
        if self.need_gource:
            resultgourcepath = get_result_path(gourcepath, "gource")
            if not file_is_ok(resultgourcepath ):
                shutil.copy(gourcepath, resultgourcepath)
            