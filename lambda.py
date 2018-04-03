#!/usr/bin/python
# -*- coding: utf-8 -*-

#匿名函数

abc = lambda x, y: x*y;
 
print(abc(1,2))

#切片
# 1. 从哪里开始  可以是负数，就是倒数
# 2. 到哪里结束
# 3. 间隔多少 step
arr = list(range(100))

print(arr[0:10])

print(arr[:50:5])