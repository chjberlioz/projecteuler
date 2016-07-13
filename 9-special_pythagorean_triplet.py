#!/usr/bin/env python

c = 1

while c < 500:
	a = 1
	while a < 500:
		if 1000*(500-c) == a*(1000-a-c): print a*(1000-a-c)*c
		a += 1
	c += 1
