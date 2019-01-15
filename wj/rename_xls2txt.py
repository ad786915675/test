import os

path=os.path.abspath('.')
path=os.path.join(path,'data')
for root,dirs,files in os.walk(path):
    #开始处理文件
    for file in files:
        if(file=='.DS_Store'):
            continue
        else:
            oldname=os.path.join(path,file)
            newname=os.path.join(path,(str(file)[:str(file).rindex('.')]+".txt"))
            os.rename(oldname,newname)


    # for file in files:
    #     if(file=='.DS_Store'):
    #         continue
    #     else:
    #         oldname=os.path.join(path,file)
    #         if(str(file).rfind(' ')!=-1):
    #             newname=os.path.join(path,(str(file)[:str(file).rindex(' ')]+".xls"))
    #             os.rename(oldname,newname)