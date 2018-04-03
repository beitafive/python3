#!/usr/bin/env python3
# -*- codind: utf-8 -*-
import math;
h = input('请问你的身高是（m）：');
w = input('请问你的体重是（kg）:');

h = float(h);
w = float(w);

bmi = round(w/(h*h),2);
print(bmi)

if bmi < 18.5 :
	print('太轻')
elif bmi>=18.5 and bmi<25:
	print("正常")
elif bmi>=25 and bmi<28:
	print('太重')
elif bmi>=28 and bmi<32:
	print('肥胖')
else:
	print('严重肥胖')