import random
import matplotlib.pyplot as plt

bigSum = 0
reps = 1000000
total = 0
list = []

for x in range(reps):
	party = random.randint(1,13)
	total = 0
	for i in range(party):
		serving = random.randint(1,8)
		for j in range(serving):
			calories = random.randint(40,500)
			total += calories

	list.append(total)
	bigSum += total

average = bigSum/reps
print(average, "calories per holiday season.")

plt.plot(list)

plt.show()