#!/usr/bin/env python
def even_fibonacci(n):
	if n == 1:
		return 2
	if n == 2:
		return 8
	return 4 * even_fibonacci(n - 1) + even_fibonacci(n - 2)

k = 1
sum = 0
while even_fibonacci( k ) <= 4000000:
	sum = sum + even_fibonacci( k )
	k = k +1
print sum
