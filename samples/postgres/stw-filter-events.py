# -*- coding: utf-8 -*-

def filter_events(event):
    prefixes=[
        "/Users/neilc/postgres/cvs_root/",
        "/home/projects/pgsql/cvsroot/",
        "/projects/cvsroot/"
    ]

    for p in prefixes:
        if event.filename.startswith(p):
           event.filename=event.filename.replace(p,"/") 
    return True

    

