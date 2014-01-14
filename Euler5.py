# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

num = 20
divisible = False

while divisible == False or num <= math.factorial(20):
	num = num + 20
	divisible = True
for i in range(11, 20) :
	if (num % i != 0) :
		divisible = False



print(num)
