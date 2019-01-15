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
            # print(file)
            if(True):
                infile=os.path.join(inpath,file)
                date=str(file)[:str(file).rindex('.')]
                outpath=os.path.join(path,'out',file)
                # print(infile)
                # print(date)
                # print(outpath)

                # inpath='./成交金额/2018.9.3.xls'
                # outpath='./out/2018.9.3.xls'
                # date='2018.9.3'
                datel=date.split('.')
                if(int(datel[1])<10):
                    datel[1]=days[int(datel[1])]
                if(int(datel[2])<10):
                    datel[2]=days[int(datel[2])]

                dates=''.join(datel)
                week=weeks[datetime.strptime(dates,"%Y%m%d").weekday()]
                dates='-'.join(datel)
                dates=dates+','+week

                datapath=os.path.join(path,'data')
                # datapath='./data/'

                workbook = xlrd.open_workbook(infile)
                worksheet1 = workbook.sheet_by_index(0)

                workbook2 = xlwt.Workbook() #注意Workbook的开头W要大写
                sheet1 = workbook2.add_sheet('sheet1',cell_overwrite_ok=True)

                rowtmp=['60分钟-1成交额', '60分钟-2成交额', '60分钟-3成交额', '60分钟-4成交额', '60分钟-1涨跌幅', '60分钟-2涨跌幅', '60分钟-3涨跌幅', '60分钟-4涨跌幅']

                num_rows = worksheet1.nrows
                for i in range(num_rows):
                    row = worksheet1.row_values(i)+rowtmp
                    if(i==0):
                        # print(row)
                        for j in range(len(row)):
                            sheet1.write(0,j,row[j])
                    elif(i>=61):
                        break
                    else:
                        ct=0
                        for j in range(12):
                            if(j==0):
                                file=row[j][:row[j].rindex('.')]+'.txt'
                                file=os.path.join(datapath,file)
                                print(file)
                            if(j<4 or j>=12):
                                sheet1.write(i,j,row[j])
                            else:
                                with open(file, 'r',encoding='GBK') as file_to_read:
                                    while True:
                                        if(ct>=4):
                                            break
                                        lines = file_to_read.readline() # 整行读取数据
                                        if not lines:
                                            break
                                        line= [str(i) for i in lines.split('\t')] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
                                        if((len(line)<12 and line[-1]=='\n') or len(line)<11):
                                            l.append(file)
                                        if(line[0].find('"')!=-1):
                                            line[0]=line[0][line[0].index('"')+1:line[0].rindex('"')]
                                        if(line[0]==dates):
                                            if(line[8].find('"')!=-1):
                                                line[8]=line[8][line[8].index('"')+1:line[8].rindex('"')]
                                            sheet1.write(i,j,line[8])
                                            sheet1.write(i,j+4,line[5])
                                            j+=1
                                            ct+=1
                                            if(ct>=4):
                                                break

                workbook2.save(outpath)
    print(len(set(l)))

if __name__ == '__main__':
    run()


