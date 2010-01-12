# -*- coding: utf-8 -*-
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
    event.author = event.author.lower().replace('%',"@")
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
