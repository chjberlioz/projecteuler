#!/usr/bin/env python
import math
def largest_prime_factor(n):
	k = 2
	is_prime = 0
	while k <= math.sqrt(n):
		if n % k ==0:
			return largest_prime_factor( n / k )
		else:
			k = k + 1
	return n

print largest_prime_factor( 2 )
print largest_prime_factor( 6 )
print largest_prime_factor( 10 )
print largest_prime_factor( 600851475143 )
