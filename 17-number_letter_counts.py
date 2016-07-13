#!/usr/bin/env python

dic = {0:0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6,12: 6,13: 8, 14: 8, 15: 7, 16: 7,17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}

sum = 0
for i in range(1000):
	sum += dic[i/100]
	if dic[i/100] != 0:
		sum += 7
		i = i - i / 100 * 100
		if i != 0:
			sum +=3
	if i<=20:
		sum += dic[i]

	else:
		sum += dic[i / 10 *10 ]
		sum += dic[i - i / 10 * 10]
sum += 11
print sum
