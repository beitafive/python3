#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time;

#时间戳 转 格式化时间
def stampToFormat(n=time.time()):
	#time.strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
	return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(n))
print(stampToFormat())

#print(time.strptime(stampToFormat(),'%Y-%m-%d %H:%M:%S'))

#格式化时间字符串 转 元组
def strToTuple(n=False):
	try:
		if n : # 函数根据指定的格式把一个时间字符串解析为时间元组。
			return time.strptime(n,'%Y-%m-%d %H:%M:%S')
		else:
			return '请输入！'
	except Exception:
		return '请输入类似这样的格式：2018-09-09 12:12:12'
print(strToTuple())