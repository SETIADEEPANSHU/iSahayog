#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
weightage={"twitter":1,"News articles":4,"portal":3,"grievance portal":2}
def calculate_rank(cnt,source,val):
    val/=1000
    value=weightage[source]
    if cnt==0:
        value=weightage[source]*1000
    else:
        value=val+weightage[source]
        value=(value*1000)
    return value
def r_ank(a_loc,a_category,source):
    locs=db((db.Rankings.loc==a_loc) & (db.Rankings.category==a_category)).select()
    j=0
    for location in locs:
        j+=1
        if location.loc!=None:
            a_cnt=location.twitter_cnt+location.portal_cnt+location.news_count+location.grieavance_portal
            val=location.r_ank
            val=calculate_rank(a_cnt,source,val)
            if source=='twitter':
                a_cnt=location.twitter_cnt
                db((db.Rankings.loc==location.loc) & (db.Rankings.category==location.category)).update(r_ank=val,twitter_cnt=a_cnt+1)
            elif source=='portal':
                a_cnt=location.portal_cnt
                db((db.Rankings.loc==location.loc) & (db.Rankings.category==location.category)).update(r_ank=val,portal_cnt=a_cnt+1)
            elif source=='News articles':
                a_cnt=location.news_cnt
                db((db.Rankings.loc==location.loc) & (db.Rankings.category==location.category)).update(r_ank=val,news_cnt=a_cnt+1)
            elif source=='grievance portal':
                a_cnt=location.grieavance_portal
                db((db.Rankings.loc==location.loc) & (db.Rankings.category==location.category)).update(r_ank=val,grieavance_portal=a_cnt+1)
    if j==0:
        val=calculate_rank(0,source,0)
        if source=='twitter':
            db.Rankings.insert(loc=a_loc,category=a_category,r_ank=val,twitter_cnt=1,portal_cnt=0,news_cnt=0,grieavance_portal=0)
        elif source=='portal':
            db.Rankings.insert(loc=a_loc,category=a_category,r_ank=val,twitter_cnt=0,portal_cnt=1,news_cnt=0,grieavance_portal=0)
        elif source=='News articles':
            db.Rankings.insert(loc=a_loc,category=a_category,r_ank=val,twitter_cnt=0,portal_cnt=0,news_cnt=1,grieavance_portal=0)
        elif source=='grievance portal':
            db.Rankings.insert(loc=a_loc,category=a_category,r_ank=val,twitter_cnt=0,portal_cnt=0,news_cnt=0,grieavance_portal=1)
