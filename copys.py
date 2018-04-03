#!/usr/bin/python3
# -*- codind: utf-8 -*-

# copy 这个不能当做文件名称

# 深浅拷贝

import copy

obj = {'a':123,'arr':[1,2,3]}

#仅仅是引用，obj obj1 指向同一块内存
obj1 = obj;

#浅拷贝	 第一层会开辟新内存。再往下 就是指向同样的内存；
obj2 = copy.copy(obj);

#深拷贝	 重新开辟内存。
obj3 = copy.deepcopy(obj);

obj['a'] = 1;

obj['arr'][0] = 2;

print(id(obj))
print(obj1)
print(id(obj1))

print(obj2)
print(id(obj2))

print(obj3)
print(id(obj3))

