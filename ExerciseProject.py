#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Prime = []
NoPrime = []
for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            print('%d不是质数' % num)
            NoPrime.append(num)
            break
    else:
        print('%d是质数' % num)
        Prime.append(num)
print('质数为：', Prime)
print('非指数为：', NoPrime);
'''

# 打印空心等边三角形

rows = int(input('输入行数：'))
for i in range(0, rows):
    for k in range(0, 2 * rows - 1):
        if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
            print(" * "),
        elif i == rows - 1:
            if k % 2 == 0:
                print(" * "),
            else:
                print("   "),
        else:
            print("   "),
    print("\n")
# ............................................