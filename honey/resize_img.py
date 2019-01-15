#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import os
# import matplotlib.pyplot as plt

x_s=640         #输出图片宽度像素值

def run():
    ct=0
    path=os.path.abspath('.')
    inpath=os.path.join(path,'ori')
    print("原始文件路径为："+inpath)
    outpath=os.path.join(path,"pic")
    print("输出文件路径为："+outpath)

    for root,dirs,files in os.walk(inpath):
        #判断输出文件夹是否存在
        isExists=os.path.exists(outpath)
        if not isExists:
            os.makedirs(outpath)
            print("目录创建成功:"+outpath)
        else:
            print("请先查看目录:"+outpath)
            return
        #开始处理文件
        for file in files:
            if(file=='.DS_Store'):
                continue
            ct+=1
            #获取文件名
            filename=os.path.join(root,file)
            #打开图片并获取像素值
            img = Image.open(filename)
            (x,y) = img.size
            y_s = int(y * x_s / x)
            #修改像素值并修改图片
            out = img.resize((x_s,y_s),Image.ANTIALIAS)
            outfilename=os.path.join(outpath,file)
            #保存修改后图片
            out.save(outfilename)
            print(filename+"-->"+outfilename)

    print(str(ct)+"张图片已处理")


if __name__ == '__main__':
    run()