"""
1.) Take random walk of n blocks
2.) Calculate distance from home
"""

import random


#NOTE: Each block here is a turn which can result in two blocks being travelled
def walk():
	global x,y,r

	if (x == 0) or (y == 0):
		if (x == 0) and (y == 0):
			if (random.randint(0,1) == 0):
				r = 1
				x += r
			else:
				r = 1
				y += r
		elif (x == 0):
			if (random.randint(0,1) == 0): #horizontal
				r = 1
				x += r
			else:
				if (random.randint(0,1) == 0): #vertical
					r = 1
				else:
					r = -1
				y += r
		elif (y == 0):
			if (random.randint(0,1) == 0): #horizontal
				if (random.randint(0,1) == 0): #vertical
					r = 1
				else:
					r = -1
				x += r
			else:
				r = 1
				y += 1



	else:
		if (random.randint(0,1) == 0): #horizontal
			if (random.randint(0,1) == 0):
				r = 1
			else:
				r = -1
			x += r
		else:
			if (random.randint(0,1) == 0): #vertical
				r = 1
			else:
				r = -1
			y += r


#--------------------------------------------------------------------



blocks = input("Input the number of blocks you would like to walk: ")
blocks = int(blocks)

x = 0
y = 0
r = 0


for i in range(blocks):
	walk()

distance = x + y

print(distance)

if (distance <= 4):
	print("Walk home.")
else:
	print("Take a taxi home.")











