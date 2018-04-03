#!/usr/bin/python3
# -*- codind: utf-8 -*-

#def trim(str):
#	n = 0;
#	while str[n] ==' ':
#		n = n+1;
#	h = -1;
#	while str[h] ==' ':
#		h = h-1;
#	return str[n:h+1]
	
def trim(str):
	if str[0]==' ':
		return trim(str[1:])
	elif str[-1] == ' ' :
		return trim(str[:-1])
	else :
		return str
	
print(trim('  wo men '))