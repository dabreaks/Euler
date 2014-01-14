# By Considering the terms in the Fibonacci sequence whose values do not exceed 4 million,
# find the sum of the even-valued terms.

j = 1
sum = 0
while j < 1000 :
	if j%3 == 0 :
		sum = sum + j
		j = j + 1
		if j >= 1000 :
			break
	if j%5 == 0 :
		sum = sum + j
		j = j + 1
		if j >= 1000 :
			break
	if (j%3 != 0) & (j%5 != 0) :
		j = j + 1
print(sum)
