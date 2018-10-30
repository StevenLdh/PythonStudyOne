#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
变量和格式处理
"""
# 变量和格式
exts = False
if exts:
    print('assde')
    print("true")
else:
    print("aaa")
    # 没有严格缩进，在执行时会报错
    print("false")
"""
字符串操作
"""
# 字符串操作
str = 'Hello World!'
print(str)  # 输出完整字符串
print(str[0])  # 输出字符串中的第一个字符
print(str[2:5])  # 输出字符串中第三个至第五个之间的字符串
print(str[2:])  # 输出从第三个字符开始的字符串
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 输出连接的字符串
print(str[-1])  # 重后面截取

"""
数值类型操作
"""
# !/usr/bin/python
# -*- coding: UTF-8 -*-

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表
# list集合增加值
for j in range(1,5):
    list.append(j)
print(list)

#  循环字符串
for i in 'hello world':
    print(i)
# 循环数字
for j in range(1,5):
    print(j)

"""
元组类型(元组中的元素值是不允许修改的，但我们可以对元组进行连接组合)
"""
tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出第二个至第三个的元素
print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)  # 输出元组两次
print(tuple + tinytuple)  # 打印组合的元组
len(tuple)

"""
Python 字典
"""
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 增加一个或多个元素
tinydict.update(b=2)  # 也可以 tinydict.update({‘b’: 2})
print(tinydict)

tinydict.update(c=3, d=4)
print(tinydict)

tinydict.update({'f': 6, 'g': 7})  # 即tinydict.update(字典)
print(tinydict)

#  删除一个或多个元素
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
x.pop(1)  # pop()，()里为需要删除的key值；即若x.pop(3)，则删除3:4元素。
print(x)

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
del x[1]
print(x)
"""
def remove_key(d, key):
    r = dict(d)
del r[key]
return r

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(remove_key(x, 1))
print(x)
"""