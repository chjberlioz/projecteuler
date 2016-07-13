#!/usr/bin/env python
import math

def is_prime(n):
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0: return False
		i += 1
	return True

pri = 3
num = 2
goal = 10001
while num <= goal:
	if is_prime(pri):
		num += 1
		pri += 2
	else: pri += 2

print pri-2
