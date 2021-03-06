#Ryan Kim
#Monday, October 1st
#Minesweeper Field - I had trouble with the ranges of things as well as the look around function. I searched it up but didn't fully grasp how to use it.
#https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups  -  Look Around Function
import sys
import random

#----------------------------------------------------------------
def reveal():
	global choiceX, choiceY, width, height

	choiceX = input("\nGive the x position you would like to reveal: ")
	choiceY = input("\nGive the y position you would like to reveal: ")

	choiceX = int(choiceX)
	choiceY = int(choiceY)
	#-----------------------------------------------
	if (field[choiceY][choiceX] == "B"):
		for y in range (1, height-1):
			for x in range(1, width-1):
				print(field[y][x], end = " ")
			print("")

		print("You hit a bomb! You lost!")
	#-----------------------------------------------
	elif (field[choiceY][choiceX] == "0"):

		points = []
		
		points.append([choiceY,choiceX])

		while(len(points) > 0):
			points.remove([choiceY, choiceX])
			for x in range(-1,2):
				for y in range(-1,2):
					if (field[choiceY + y][choiceX + x] == "0") and (board[choiceY + y][choiceX + x] == "#"):
						points.append([choiceY + y,choiceX + x])
						
					board[choiceY + y][choiceX + x] = field[choiceY + y][choiceX + x]





		for y in range (1, height-1):
			for x in range(1, width-1):
				print(board[y][x], end = " ")
			print("")

	#-----------------------------------------------
	elif (field[choiceY][choiceX] != "B") and (field[choiceY][choiceX] != "0"): #also could put else instead of elif statement
		board[choiceX][choiceY] = field[choiceY][choiceX]

		for y in range (1, height-1):
			for x in range(1, width-1):
				print(board[y][x], end = " ")
			print("")
	#print board without any other point showing
#----------------------------------------------------------------
#def flag():



#----------------------------------------------------------------
def surrouned():
	global choiceY, choiceX, width, height

	if (field[choiceY][choiceX] == "0"):
		board[choiceY][choiceX] = field[choiceY][choiceX]
		board[choiceY+1][choiceX] = field[choiceY+1][choiceX]
		board[choiceY-1][choiceX] = field[choiceY-1][choiceX]
		board[choiceY][choiceX+1] = field[choiceY][choiceX+1]
		board[choiceY][choiceX-1] = field[choiceY][choiceX-1]
		board[choiceY+1][choiceX+1] = field[choiceY+1][choiceX+1]
		board[choiceY+1][choiceX-1] = field[choiceY+1][choiceX-1]
		board[choiceY-1][choiceX+1] = field[choiceY-1][choiceX+1]
		board[choiceY-1][choiceX-1] = field[choiceY-1][choiceX-1]
		


width = input("Width: ")
height = input("Height: ")
bombs = input("Bombs: ")

width = int(width)
height = int(height)
bombs = int(bombs)

width += 2
height += 2

board = []

board = [["#"]*width for x in range(height)]

field = []

field = [["0"]*width for x in range(height)]



#Makes the gutter all 1 so that there is no out of range problem
board[0] = [1]*width
board[-1] = [1]*width
for j in board:
	j[0] = 1
	j[-1] = 1



#Print
for y in range (1, height-1):
	for x in range(1, width-1):
		print(board[y][x], end = " ")
	print("")


count = 0
while (count < bombs):
	randomW = random.randint(1,width-2)
	randomH = random.randint(1,height-2)

	field[randomH][randomW] = "B"	

	count += 1


for y in range(1, height-1):
	for x in range(1, width-1):
		if (field[y][x] == "B"):
			
			if (field[y][x+1] != "B"):
				if (field[y][x+1] == "0"):
					field[y][x+1] = 1
					field[y][x+1] = int(field[y][x+1])
				else:
					field[y][x+1] += 1

			if (field[y][x-1] != "B"):
				if (field[y][x-1] == "0"):
					field[y][x-1] = 1
					field[y][x-1] = int(field[y][x-1])
				else:
					field[y][x-1] += 1

			if (field[y+1][x] != "B"):
				if (field[y+1][x] == "0"):
					field[y+1][x] = 1
					field[y+1][x] = int(field[y+1][x])
				else:
					field[y+1][x] += 1

			if (field[y-1][x] != "B"):
				if (field[y-1][x] == "0"):
					field[y-1][x] = 1
					field[y-1][x] = int(field[y-1][x])
				else:
					field[y-1][x] += 1

			if (field[y+1][x+1] != "B"):
				if (field[y+1][x+1] == "0"):
					field[y+1][x+1] = 1
					field[y+1][x+1] = int(field[y+1][x+1])
				else:
					field[y+1][x+1] += 1

			if (field[y+1][x-1] != "B"):
				if (field[y+1][x-1] == "0"):
					field[y+1][x-1] = 1
					field[y+1][x-1] = int(field[y+1][x-1])
				else:
					field[y+1][x-1] += 1

			if (field[y-1][x-1] != "B"):
				if (field[y-1][x-1] == "0"):
					field[y-1][x-1] = 1
					field[y-1][x-1] = int(field[y-1][x-1])
				else:
					field[y-1][x-1] += 1

			if (field[y-1][x+1] != "B"):
				if (field[y-1][x+1] == "0"):
					field[y-1][x+1] = 1
					field[y-1][x+1] = int(field[y-1][x+1])
				else:
					field[y-1][x+1] += 1


#User Input
choice = input("Choose your option:\n 1.) Reveal - Choose a spot on the board and reveal whether there is a bomb or not\n 2.) Flag - Mark a spot on the board where you think there is a bomb\n\n Option: ")

#use a function here
if (choice == "1") or (choice == "reveal")  or (choice == "Reveal"):
	reveal()

#if (choice == "2") or (choice == "flag") or (choice == "Flag"):
	#flag position
	#flag function
#-----------------------------------------------




"""
if (field[y-1][x+1] != "B"):
				field[y-1][x+1] = int(field[y-1][x+1])
				field[y-1][x+1] += 1
"""

"""
for y in range (1, height-1):
	for x in range(1, width-1):
		print(field[y][x], end = " ")
	print("")
"""



#1.) Corner numbers - adding 2 to h and w
#2.) Adding more than 1 bomb - removing and inserting 0 - need to regenerate random numbers