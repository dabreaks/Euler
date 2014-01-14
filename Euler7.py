# What is the 10 001st prime number?

#SIEVE OF ERATOSTHENES

n = 10001

arr = [2, 3]

c= 4

while(len(arr) < n):
	if (c % 2 != 0 & c % 3 != 0):
		t = 4
		while(t * t <= c):
			if(c % t == 0):
				break
			t=t+1
		if(t*t > c):
			arr.append(c)
	c = c+1

print(arr[n-1])
