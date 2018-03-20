#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
import json
import os


def strip_write(x):
    stck, i, lst, top = [], 0, [], -1
    while x[i]<'{':
        i += 1
    while i<len(x):
        lst.append(x[i])
        if x[i] == '{':
            stck.append(x[i])
        if stck[top] == '{' and x[i] == '}':
            stck.pop()
        if len(stck) == 0:
            break
        i += 1
    x1 = ''.join(lst)
    return x1


def replace_write(x):
    lst = []
    i = 0
    while i < len(x):
        if x[i] == '\\':
            i += 1
            continue
        lst.append(x[i])
        i += 1
    x = ''.join(lst)
    return x


def rearrange_write(x):
    lst=[0]
    while True:
        try:
            i = x.index('href',lst[len(lst)-1]) + 5
            lst.append(i); i+=1
            while x[i]!='\"':   i+=1
            lst.append(i)
            i = x.index('rel=',lst[len(lst)-1]) + 4
            lst.append(i); i += 1
            while x[i]!='\"':   i+=1
            lst.append(i)
        except ValueError:
            break
    i,l,k=0,[],1
    while i < len(x):
        if k<len(lst) and i==lst[k]:
            l.append('\\\"')
            k += 1
            i += 1
        else:
            l.append(x[i])
            i += 1
    y = ''.join(l)
    return y

def json_par(file_name):
    f = open(file_name, 'r')
    x = f.read()
    f.close()
    x = strip_write(x)
    xx=os.path.join(current.request.folder, 'private', 'data_file.json')
    f = open(xx, 'w')
    x = replace_write(x)
    x = rearrange_write(x)
    f.write(x)
    f.close()

    with open(xx, 'r') as f:
        data = json.load(f)
        if data["place"]==None:
            db.Testing.insert(Texts=data["text"],u_name=data["user"]["screen_name"],u_loc=data["user"]["location"],isRetweet=data["retweeted"])
        else:
			db.Testing.insert(Texts=data["text"],u_name=data["user"]["screen_name"],u_loc=data["user"]["location"],t_loc=data["place"]["name"],isRetweet=data["retweeted"])
    f.close()
    return locals()
