#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

it = iter('abcdef')   	#创建迭代器对象

while True:
	try:
		print(next(it))
	except StopIteration:	#如果出错
		sys.exit();			#退出程序
		
#斐波那契

def fbnq(n):	#生成器
	a,b,num = 0,1,0;
	while True:
		if num > n :
			return 
		yield b          #相当于 函数输入b 
		a , b = b , a+b;
		num += 1;
f = fbnq(11)	#迭代器，由生成器返回生成
print(type(f))  #generator
while True:
	try:
		print(next(f), end=' ')
	except StopIteration:
		sys.exit();