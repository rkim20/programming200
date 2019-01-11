import random
import matplotlib.pyplot as plt

results = []

for i in range(1000):
	total = 0
	for j in range(10):
		flip = random.randint(0,1)
		total += flip
	results.append(total)

display = [0 for i in range(11)]
for i in range(len(results)):
	display[results[i]] += 1

plt.plot(display, 'r^')
plt.bar([0,1,2,3,4,5,6,7,8,9,10], display, color=(0.5, 0., 0.5, 1.0))

plt.show()
