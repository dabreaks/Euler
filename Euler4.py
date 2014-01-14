# Find the largest palindrome made from the product of two 3 digit numbers

j = 999
i = 999
pdrome = False
switch = True
product = None
max = 0
for o in range(500, 999):
	for m in range(500, 999) :
		product = o * m
		word = str(product)
		pdrome = True
		for p in range(0, (len(word)//2)) :
			if word[p] != word[-p-1] :
				pdrome = False
		if pdrome == True :
			if product > max :
				max = product
		


print(max)
