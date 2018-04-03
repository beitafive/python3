#!/usr/bin/python3
# -*- coding: utf-8 -*-

#codecs.open(文件名称,目的,编码)
#编码默认是GBK
import os, codecs;

#获取当前目录下文件
list = os.listdir();


for x in list:
	#获取py文件
	if x[x.rfind('.'):].upper() == '.PY':
		file = codecs.open(x,"r",'utf-8')
		print(file.name)
		print(file.read(20))
	elif x.rfind('.') == -1:
		print(os.listdir(x))
		print("文件夹：",x)
	else:
		try:
			file2 = open(x,"r","GBK")
			print(file2.name)
			print(file2.read(20))
		except:
			file2 = codecs.open(x,"r","utf-8")
			print(file2.name)
			print(file2.read(20))