import random

def trial():
	counter = 0
	for x in range(10):
		num = random.randint(0,1)
		if (num == 0):
			counter += 1
	return counter




#Main-----------------------------------------
smallTotal = []

for x in range(10):
	smallTotal.append(trial())


print(smallTotal)