import math

# Find sum of all prime numbers less than 2 million

# IMPLEMENT THE SIEVE OF ERATOSTHENES

num = []

#print(len(num))
primes = []
primes.append(2)
prime_sum = 2
#print(len(num))

i = 3
while (i < 1999999) :
	num.append(i)
	i = i+2
print(len(num))
for i in num:
	prime = True
	for j in primes:
		if i % j == 0:
			prime = False
			break
	if prime == True:
		prime_sum = prime_sum + i
		primes.append(i)
print(primes)
print(prime_sum)

# while the list is not empty
#    pop the first element of the list to primes
#    for each element in the list
#       if any subsequent element of the list is a multiple of the popped item
#          remove the element from the list

# return the list of primes
#length = len(num)

#while (num) :
#	i = num[0]
#	print(i)
#	num.remove(i)
#	primes.append(i)
#	for j in num :
#		if (j % i == 0 ):
#			num.remove(j)
#	length = len(num)
#	print(length)
#print(primes)

