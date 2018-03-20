"""
This file contains 3 methods to create and update problem_id, solution_id and college_id
"""
import os
def generate_pid(request):
    x=os.path.join(request.folder, 'private', 'id.txt')
    f = open(x, 'r')
    lst = f.readlines()
    cur_pid = int(lst[0]) + 1
    lst[0] = str(cur_pid) + '\n'
    f.close()
    f = open(x, 'w')
    f.writelines(lst)
    f.close()
    return cur_pid


def generate_cid(request):
    x=os.path.join(request.folder, 'private', 'id.txt')
    f = open(x, 'r')
    lst = f.readlines()
    cur_cid = int(lst[1]) + 1
    lst[1] = str(cur_cid) + '\n'
    f.close()
    f = open(x, 'w')
    f.writelines(lst)
    f.close()
    return cur_cid

def generate_sid(request):
    x=os.path.join(request.folder, 'private', 'id.txt')
    f = open(x, 'r')
    lst = f.readlines()
    cur_sid = int(lst[2]) + 1
    lst[2] = str(cur_sid) + '\n'
    f.close()
    f = open(x, 'w')
    f.writelines(lst)
    f.close()
    return cur_sid
def destroy_pid(request):
    x=os.path.join(request.folder, 'private', 'id.txt')
    f = open(x, 'r')
    lst = f.readlines()
    cur_pid = int(lst[0]) - 1
    lst[0] = str(cur_pid) + '\n'
    f.close()
    f = open(x, 'w')
    f.writelines(lst)
    f.close()
    #return cur_pid


def destroy_cid(request):
    x=os.path.join(request.folder, 'private', 'id.txt')
    f = open(x, 'r')
    lst = f.readlines()
    cur_cid = int(lst[1]) - 1
    lst[1] = str(cur_cid) + '\n'
    f.close()
    f = open(x, 'w')
    f.writelines(lst)
    f.close()
    #return cur_cid

def distroy_sid(request):
    x=os.path.join(request.folder, 'private', 'id.txt')
    f = open(x, 'r')
    lst = f.readlines()
    cur_sid = int(lst[2]) - 1
    lst[2] = str(cur_sid) + '\n'
    f.close()
    f = open(x, 'w')
    f.writelines(lst)
    f.close()
    #return cur_sid
