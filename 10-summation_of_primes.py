#!/usr/bin/env python

import math

def is_prime(n):
	i = 2
	while i<=math.sqrt(n):
		if n % i == 0: return False
		i += 1
	return True

sum = 2
num = 3

while num < 2000000:
	if is_prime(num):
		sum += num
	num += 2
print sum
