#!/usr/bin/env python
pro = 1
for i in range(101):
	if i != 0:
		pro *= i

sum = 0
while pro >= 10:
	sum = sum + pro%10
	pro = ( pro- pro%10) / 10
sum += pro
print sum
