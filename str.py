#!/usr/bin/python3
# -*- coding: utf-8 -*-

s = '1伍昭乾W111'

# 第一个字符转成大写，其他变为小写；第一个字符不是字母的话，其他还是会变成小写
print(s.capitalize())

# 搜索字符在字符串出现的次数，1.搜索字符 2.开始位置（开头） 3.结束位置（结尾）
print(s.count('1'))

# str.encode() 	 编码   
# bytes.decode() 解码
print(s.encode('utf-8'))

print(s.encode('utf-8').decode('utf-8','strict'))

# str.endswith() 判断字符串结尾， 可以指定字符串位置
print(s.endswith('W',3,5))

# str.find()   方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
#	如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
# str.index()  不存在的话会报错
print(s.find('1',3))

s2 = 'wzhaoqianWWWWW';
print(s2.lower()) #  转小写
print(s2.upper()) #  转大写

s3 = '  111  123   1111  ';
# str.strip() 去除首尾指定字符  默认空格
print(s3.strip())
print(s3.strip().strip('1'))