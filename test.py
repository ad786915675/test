# -*- coding:utf-8 -*-

def run():
    sites = ["Baidu", "Google","Taobao","Runoob"]
    for site in sites:
        print("循环数据 " + site)
        if site == "Runoob":
            print("菜鸟教程!")
            break
    else:
        print("没有循环数据!")
    print("完成循环!")

if __name__=='__main__':
    run()