#!/usr/bin/env python
year = 1901
residual_day = 1


sunday = 0

while year<=2000:
	sunday = sunday + (residual_day+31)/7
	if year%4!=0 or (year%100 ==0 and year%400 != 0):
		residual_day = (residual_day +365)%7
	else: residual_day = (residual_day +366)%7
	year += 1

print sunday
