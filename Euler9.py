import timeit

#There exists one pythagorean triplet for which a + b + c = 1000

# Find the product abc


def ktest(a, b, c):
	k = 1
	su = a + b +c
	while (su <=1000 ) :
		if su == 1000 :
			prod = a * b * c * k * k * k
			return(prod)
		k = k + 1
		su = k*(a+b+c)
	return 0


# Find py triplet
def main() :
	a = 3
	b = 4
	c = 5

	for i in range(2, 998):
		r = int(i*i / 2)
		for s in range(1, r):
			if (r % s == 0):
				t = r / s
				a = i + s
				b = i + t
				c = i + s + t

				# test for k
				prod = ktest(a, b, c)	
				if prod > 0 :
					print(prod)
					break
		if prod > 0:
			break

main()

#t = timeit.Timer("main()", "from ")
#t.timeit()


