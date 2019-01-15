#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import filecmp

l=[]
flag=[]
d=[]
def run():
    path=os.path.abspath('.')
    inpath=os.path.join(path,'tmp')
    for root,dirs,files in os.walk(inpath):
        for file in files:
            l.append(str(file))

    # print(l)

    for i in range(len(l)):
        flag.append(1)

    for i in range(len(l)):
        print(str(i)+":"+str(l[i]))
        if(flag[i]==0):
            continue
        f1=os.path.join(inpath,str(l[i]))
        for j in range(i+1,len(l)):
            if(flag[j]==0):
                continue
            f2=os.path.join(inpath,l[j])
            if(filecmp.cmp(f1,f2)):
                os.remove(f2)
                flag[j]=0
                print("\tdelete:"+f2)
                d.append(f2)
    for i in range(len(d)):
        print(d[i])

if __name__=='__main__':
    run()