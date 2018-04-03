#!/usr/bin/python3
# -*- coding: utf-8 -*-

print([[x,x*2] for x in range(6) if x>2] )

arr = [[3, 6], [4, 8], [5, 10]];
#双循环 2*3矩阵  变为 3*2矩阵
print([[row[i] for row in arr] for i in range(2)])

a1 = list(range(1,10,1));
a2 = list(range(1,10,1));
a2.reverse(); # 倒序

#print([[x*y for x in a1] for y in a2])
a1.insert(len(a1),10)
print(a1)