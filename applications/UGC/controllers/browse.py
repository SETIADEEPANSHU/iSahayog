# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from browse.py")

def manage_problems():
    grid=SQLFORM.grid(db.Problems)
    return locals()
