import random
from collections import Counter
import matplotlib.pyplot as plt

prices = []
reps = 1000000
sum = 0

for i in range(reps):
	totalPrice = 0
	chances = random.randint(1,4)
	for j in range(chances):
		items = random.randint(1,4)
		for k in range(items):
			cost = random.randint(2,13)
			totalPrice += cost
	prices.append(totalPrice)
	sum += totalPrice

average_per_week = sum/reps
price_results = sorted(Counter(prices).items())

print("On average, you will spend $" + str(average_per_week) + " per week on ordering food.")

graph_data = []
x_data = []
for tuples in price_results:
	graph_data.append(tuples[1])
	x_data.append(tuples[0])

plt.plot(x_data,graph_data)
plt.show()

