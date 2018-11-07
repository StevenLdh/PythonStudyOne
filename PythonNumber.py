#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Python随机数函数
"""
import cmath
import random
import math
print(cmath.sqrt(9))
# 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
print(random.choice(range(9)))
# 随机生成下一个实数，它在[0,1)范围内。
print(random.random())
# 随机生成下一个实数，它在[x,y]范围内。
print(random.uniform(1, 5))
# 返回x的反余弦弧度值。
print(math.acos(0.64))
print('\a')