#!/usr/bin/env python
import math
def is_palindrome(n):
	o = n
	m = 0
	while n >= 10:
		m = m * 10 + n % 10
		n = n / 10
	m = m * 10 + n
	if m == o:
		return 1
	return 0

n = 999 * 999
is_ok = 0
while is_ok == 0:
	if is_palindrome( n ) == 0:
		n = n - 1
	else:
		k = 999
		while k >= math.sqrt( n ):
			if n % k == 0:
				is_ok = 1
				print n
				break
			else:
				k = k - 1
		n = n - 1
