# -*- coding: utf-8 -*-
# try something like
from slackclient import SlackClient
def join(uid):
    v=db(db.Slck.user_id==uid).select(db.Slck.slack_pass)
    sc = SlackClient(v)
    x = sc.api_call("channels.join",name="MyChannel")
    x=x["channel"]["id"]
    y = db(db.Col).select(db.Col.ch_id)
    if y==None:
        db.Col.insert(ch_id=x)
    
def postMessage():
    v=db(db.Slck.user_id==uid).select(db.Slck.slack_pass)
    sc = SlackClient(v)
    x=sc.api_call("chat.postMessage",name="MyChannel",text=request.args[0])
    y=db(db.Col).select(db.Col.ch_id).first()
    x=sc.api_call("channels.history",channel=y.ch_id)
    db(db.Col.ch_id==y.ch_id).update(json_data=x)
