#!/usr/bin/env python3
# -*- codind: utf-8 -*-

def fib():
	zero = 0;
	num = input("请输入一个大于0的数字：");
	num = int(num);
	if num <= 0 :
		print('输入有误！');
		fib()
		return
	maxNum = input("请输入一个最大数字：");
	maxNum = int(maxNum)
	if maxNum <= num :
		print('必须大于第一个输入的数字');
		fib()
		return 1
	while num < maxNum:
		zero = int(num);
		num = zero + int(num);
		print(zero , num)
		
fib();
	
