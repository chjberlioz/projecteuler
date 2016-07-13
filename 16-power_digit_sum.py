#!/usr/bin/env python

sum = 0

k = pow(2,1000)

while k>=10:
	sum += k%10
	k = (k - k%10)/10

sum += k
print sum
