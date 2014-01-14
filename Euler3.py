 # What is the largest prime factor of 600851475143?

j = 600851475143
i = 2
sum = None
while i !=  j :
	if j % i == 0 :
		print(i)
		sum = i
		j = j/i
	else:
		i = i + 1
		sum = i


print(sum)
