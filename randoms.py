#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

num = 0;
def rand(n):
	print(num)	#函数内部不可改变外部变量的值，可以通过传参
	n = n + 1
	print(n)
	x = random.choice(range(100))
	y = random.choice(range(200))
	print(x , y)
	if x < y:
		print('小')
		rand(n);
		return;
	elif x == y:
		print('豹子')
	else :
		print('大')
		rand(n)
		return;
rand(num)

# choice只能传入一个列表，元组或字符串		
# randrange 可以传入一个参数，或者三个参数（start，strop，step）
# shuffle 重新排序
# uniform 传入两个参数（x，y） x < num < y