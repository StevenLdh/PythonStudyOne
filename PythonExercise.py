#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# 九九乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}\t".format(j,i,i*j),end="")
    print()
"""
# 用户输入摄氏温度
"""
# 接收用户输入
celsius = float(input('输入摄氏温度: '))
# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f ' % (celsius, fahrenheit))
"""
# 简单计算器实现
"""
# 定义函数
#  相加
def add(x, y):
    return x + y
#  相减
def subtract(x, y):
    return x - y
# 相乘
def multiply(x, y):
   return x * y
# 相除
def divide(x, y):
    return x / y
# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")
choice = input("输入你的选择(1/2/3/4):")
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("非法输入")
"""
# 生成日历实例
"""
# 引入日历模块
import calendar
# 输入年份
yy = int(input("请输入年份："))
mm = int(input("请输入月份："))
# 打印结果
print(calendar.month(yy,mm))
"""
# 计算每个月天数
"""
# 引入日历模块
import  calendar
# 输入年份
yy = int(input("请输入年份："))
mm = int(input("请输入月份："))
# 获取当前月份的天数
monthrange = calendar.monthrange(yy,mm)
print(monthrange)
"""
# 获取昨天日期
# 引入日历模块
import datetime
def getyestertoday(days):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=days)
    return today-oneday
print(getyestertoday(2))

