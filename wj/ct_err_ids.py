#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import xlwt
import os
from datetime import datetime

print('test2')

weeks=['一','二','三','四','五']
days=['00','01','02','03','04','05','06','07','08','09']
path=os.path.abspath('.')
l=[]

def run():
    outpath=os.path.join(path,'out')
    for root,dirs,files in os.walk(outpath):
        for file in files:
            if(file=='.DS_Store'):
                continue
            outfile=os.path.join(outpath,file)
            # print(outfile)

            workbook = xlrd.open_workbook(outfile)
            worksheet1 = workbook.sheet_by_index(0)
            for i in range(worksheet1.nrows):
                row = worksheet1.row_values(i)
                if(row[4]==''):
                    l.append(row[0][:row[0].rindex('.')])
                    print(row)

    s=set(l)

    workbook2 = xlwt.Workbook() #注意Workbook的开头W要大写
    sheet1 = workbook2.add_sheet('sheet1',cell_overwrite_ok=True)
    ct=0
    for i in s:
        sheet1.write(ct,0,i)
        ct+=1
    workbook2.save('./err.xls')



if __name__ == '__main__':
    run()


