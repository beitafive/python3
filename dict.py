#!/usr/bin/env python3
# -*- codind: utf-8 -*-
# 字典特性
# 1： 不允许同一个键出现两次，后者覆盖；
# 2:  键不可变，可以用number，string，tuple；
dict = {'a':1,'b':123,12:12}
print(dict)

dict[12] = 13;	#更新
dict[13] = 14;  #添加
print(dict)

del dict[12];   #删除
dict.pop(13);   #删除
print(dict)

dict.clear();   #清空字典
print(dict)

del dict;       #删除字典

