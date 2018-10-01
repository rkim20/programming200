#Ryan Kim
#Monday, October 1st
#Minesweeper Field - I had trouble with the ranges of things as well as the look around function. I searched it up but didn't fully grasp how to use it.
#https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups  -  Look Around Function


import sys
import random

"""
i = [[1,2,3],[4,5,6],[7,8,9]]

print (i[1][0])

= 4
"""

width = int(sys.argv[1])
height = int(sys.argv[2])
bombs = int(sys.argv[3])

field = []

field = [[0]*width for x in range(height)]

for x in range(bombs):
	randomW = random.randint(0,width)
	randomH = random.randint(0,height)

	field[randomH].remove(0)
	field[randomH].insert(randomW,"B")


for x in range(height):
	for y in range(width):
		if (field[x][y] == "B"):
			field[x+1].insert(y, 1)


for x in range(len(field)):
	print(*field[x])