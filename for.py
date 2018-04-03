#!/usr/bin/env python3
# -*- codind:utf-8 -*-

sum = 0;
obj = {
		'name':123,
		'Age':0,
		'a':12
	  }
# for循环中 不可删除 添加字典
keyList = list(obj.keys())
valueList = list(obj.values())
for n in keyList:
	print(n)
for x in valueList:
	print(x)
	
print(obj)