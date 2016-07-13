#!/usr/bin/env python

def num_step(n):
	k = 1
	while n != 1:
		if n % 2 == 0:
			k += 1
			n = n / 2
		else:
			k += 1
			n = 3*n + 1
	return k

longest = [1, 1]

for i in range(1000000):
	if i >0:
		step = num_step(i)
		if step > longest[0]:
			longest[0] = step
			longest[1] = i

print longest[1]
