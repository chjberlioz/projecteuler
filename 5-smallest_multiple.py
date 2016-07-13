#!/usr/bin/env python
num = 1
i = 1
while i <= 20:
	num *= i
	i += 1

def is_divisable(n):
	i = 2
	while i <= 20:
		if n % i != 0: return False
		i += 1
	return True

b = [2, 3, 5, 7, 11, 13, 17, 19]

for i in b:
	s = 1
	while s == 1:
		temp = num / i
		if is_divisable(temp): num = temp
		else: s = 0

print num
