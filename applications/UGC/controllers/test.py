# -*- coding: utf-8 -*-
# try something like
from gluon import current
tt=local_import('saveTweets')
jp=local_import('json_parsing')
dt=local_import('doTweet')
def index():
    tt.fetchTweets()
    #jp.db=db
    #jp.request=request
    #jp.session=session
    #jp.json_par(auth,current)
    #session.a=1
    #texts="hello india this is tweet usingcrontab."+str(session.a)
    #session.a+=1
    #im_path=""
    #dt.posts(texts,im_path)
    return dict()
def queue_task():
    return "Kuchh nahi"
