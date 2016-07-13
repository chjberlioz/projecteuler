#!/usr/bin/env python

def multiples(n, k):
	num = n / k
	if n % k != 0:
		return ( k * (1 + num) * num ) / 2
	else:
		return ( k * num * (num - 1)) / 2

print multiples(1000, 3) + multiples(1000, 5) - multiples(1000, 15)
