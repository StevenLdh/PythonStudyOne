#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入内容
"""
str = input("请输入：")
print("你输入的内容是: ", str)
"""
"""
# 打开一个文件（写入内容）
fo = open("D:/test.txt", "w")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)
fo.write("www.runoob.com!\nVery good site!\n")
fo.close()
"""
"""
# 打开一个文件读取内容
fo = open("D:/test.txt", "r+")
print("文件名: ", fo.name)
str = fo.read(5)
print("读取的字符串是 : ", str)
postion=fo.tell()
print("当前的位置：", postion)
fo.close()
"""
import os
"""
# 重命名文件test.txt到tests.txt
os.rename("D:/test.txt", "D:/tests.txt")
"""
"""
# 删除指定的文件
os.remove("D:/tests.txt")
"""
os.mkdir("D:/text.txt")






