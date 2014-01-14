# By Considering the terms in the Fibonacci sequence whose values do not exceed 4 million,
# find the sum of the even-valued terms.

fib1 = 1
fib2 = 2
sum = 0
while fib2 < 4000000 :
	if fib2%2 == 0 :
		sum = sum + fib2

	temp = fib1 + fib2
	fib1 = fib2
	fib2 = temp
print(sum)
