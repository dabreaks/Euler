# What is the largest product of 5 consecutive digits of Euler8.txt?

#Dynamic programming

list = []

with open('Euler8.txt', 'r') as f:
	list = f.read()
list = str(list)
top = 0
for i in range(0, len(list)-5):
	p = int(list[i]) * int(list[i+1]) * int(list[i+2]) * int(list[i+3]) * int(list[i+4])
	if p > top:
		top = p

print(top)
