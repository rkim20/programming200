#Ryan Kim
#January 11, 2019
#On my honor, I have neither given nor received unauthorized aid
"""
https://www.riskamp.com/files/RiskAMP%20-%20Monte%20Carlo%20Simulation.pdf
- I used this source to understand the Monte Carlo simulation more

"""

#1.) The longest walk is 22 blocks. The Monte Carlo method runs through thousands of trials to find an accurate percentage that fits into the description. In this case, that is walking home 50% of the time. By setting the number of trials higher, the accuracy of the answer increases.

#2.) From my brief research, the Monte Carlo simulation works by computing many repetitions of the same model or program, each time having a completely new start so that the results aren't altered or affected by anything and can be completely unflawed. By this I mean no specific choice or number is always chosen, but it is generated randomly. After running through such program, the computer takes the results and presents the results of the outcoms. Therefore, the probability list or results are from thousands of trials. Although this simulation can't be perfect every time, it draws a general picture of probability.

#3.)
import random

x = 0
y = 0
target = 0

dartLocations = []

for x in range(9):
	dartLocations.append(x+1)


"""
Dart Locations
1 - top left
2 - top center
3 - top right
4 - middle left
5 - middle center
6 - middle right
7 - bottom left
8 - bottom center
9 - bottom right
"""

reps = 100000

for x in range(reps):
	loc = random.randint(0,9)
	if (loc == 2) or (loc == 4) or (loc == 5) or (loc == 6) or (loc == 8):
		target += 1

print("Number of times you hit the target:", target)

target = target*4

number = target/reps

print("Number:", number)


#The output goes from around 1.7 to 2.4 at 100 trials. However, as the number of trials gets higher, the number gets more and more specific, circling between 1.98 and 2.01









