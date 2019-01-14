#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 引用插件
import pymongo
'''
判断数据库是否存在
'''
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = myclient.list_database_names()
if "stevendb" in dblist:
    print("数据库已存在")
# 访问数据库
mydb = myclient["stevendb"]
# 指定表
mycol = mydb["runoob"]
# 添加数据（插入单行）
'''
mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
print(mycol.insert_one(mydict).inserted_id)
'''

# 添加数据（插入多行）
'''
mylist = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
  { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
print(mycol.insert_many(mylist).inserted_ids)

'''
# 修改数据（单个修改）
'''
myquery = { "alexa": "10000" }
newvalues = { "$set": { "alexa": "12345" } }
mycol.update_one(myquery,newvalues)
'''
# 修改数据（多行修改）
'''
myquery = { "name":{ "$regex": "^F" } }
newvalues = { "$set": { "name": "steven" } }
mycol.update_many(myquery,newvalues)
'''
# 删除数据（单行删除）
'''
myquery={"name":"QQ"}
mycol.delete_one(myquery)
'''
# 删除数据（多行删除）
'''
myquery = { "name":{ "$regex": "^F" } }
mycol.delete_many(myquery)
'''
# 查询数据
'''
for item in mycol.find().sort("alexa"):
    print(item)
'''

# 查询条件 AND OR
'''
print("---------AND条件（where alexa='100' and name='Taobao' ）-----")
for item in mycol.find({"alexa":"100","name":"Taobao"}):
    print(item)
print("---------OR条件（where alexa='100' or name='Taobao' ）-----")
for item in mycol.find({"$or": [{"alexa":"100"},{"name":"Taobao"}]}):
    print(item)
'''

# 查询  $type 操作符
'''
for item in mycol.find({"title":{"$type":2}}):
    print(item)
'''
# 查询 limit skip
'''
for item in mycol.find().limit(2).skip(15):
    print(item)
'''
# aggregate() 方法
'''
for item in mycol.find({"alexa":{"$gt":"100"}}):
    print(item)
'''

# 聚合查询
'''
rules = [
    {"$match":{"likes":{"$gte":102,"$lte":109}}},
    {"$group":{ "_id": "$name", "count":{ "$sum": 1}}}
]
for item in mycol.aggregate(rules):
    print(item)
'''
# 数据库引用
'''
var relust=db.myaddress.findOne();
var user=relust.address;
db[user.$ref].findOne({"_id":user.$id});
'''