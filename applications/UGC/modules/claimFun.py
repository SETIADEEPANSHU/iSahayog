#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
def claim():
    pp=request.args
    solution= db(db.Solutions.p_id==pp).select()
    if solution==None:
        db.Solutions.insert(p_id=pp)
    solution= db(db.Solutions.p_id==pp).select()
    response.flash=pp
    return locals()
