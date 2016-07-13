#!/usr/bin/env python
sum = 0
sum1 = 0
for i in range(101):
	sum += i * i
	sum1 += i
sum1 *= sum1
print sum1-sum
