#!/usr/bin/env python
import math
def triangle_number(n):
	return n*(1+n)/2

def num_of_divisiors(n):
	num = 0;
	i = 1;
	while i < math.sqrt(n):
		if n % i == 0:
			num += 1
		i += 1
	num *= 2
	if n / math.sqrt(n) == math.sqrt(n):
		num += 1
	return num

i = 1
while num_of_divisiors(triangle_number(i)) <= 500:
	i += 1
print triangle_number(i)

