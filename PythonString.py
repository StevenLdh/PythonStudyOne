#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  string
"""
Python 字符串格式化
"""
# 格式化字符串
print("My name is %s and weight is %d kg!" % ('Steven', 27))

# python的字符串内建函数
strs = "this a Python Project!"
print(strs.capitalize())

# 字符串join()的使用方法
str = "-"
seq = ("a", "b", "c")
print(str.join(seq))
list=['1','2','3','4','5']
print(''.join(list))
print(strs.lower())
print(max(strs))
print(min(strs))

# Python format 格式化函数
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的


