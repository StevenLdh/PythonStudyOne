#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 可写函数说明
def printinfo(arg1, *vartuple):
    # "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
#  调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

# 匿名函数
sum=lambda arg1,arg2:arg1+arg2
print("相加后的值为 :",sum(10,20))
print("相加后的值为 :",sum(20,20))