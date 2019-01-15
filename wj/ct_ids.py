#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import xlwt
import os
from datetime import datetime

weeks=['一','二','三','四','五']
days=['00','01','02','03','04','05','06','07','08','09']
path=os.path.abspath('.')
l=[]

def run():
    inpath=os.path.join(path,'in')
    for root,dirs,files in os.walk(inpath):
        for file in files:
            infile=os.path.join(inpath,file)
            print(infile)

            workbook = xlrd.open_workbook(infile)
            worksheet1 = workbook.sheet_by_index(0)

            num_rows = worksheet1.nrows
            for i in range(num_rows):
                row = worksheet1.row_values(i)
                if(i==0):
                    pass
                elif(i>=61):
                    break
                else:
                    l.append(row[0])

    s=set(l)

    workbook2 = xlwt.Workbook() #注意Workbook的开头W要大写
    sheet1 = workbook2.add_sheet('sheet1',cell_overwrite_ok=True)
    ct=0
    for i in s:
        sheet1.write(ct,0,i)
        ct+=1
    workbook2.save('./all.xls')



if __name__ == '__main__':
    run()


