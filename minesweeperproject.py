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
		
		points.append([choiceY, choiceX])

		checked = []

		while(len(points) > 0):

			var1 = points[0]
			choiceY = var1[0]
			choiceX = var1[1]

			points.remove(var1)
			checked.append(var1)

			for x in range(choiceY-1,choiceY+2):
				for y in range(choiceX-1,choiceX+2):

					if (field[x][y] == "0") and (board[x][y] == "#"):
						points.append([x,y])
						
					board[x][y] = field[x][y]




		for y in range (1, height-1):
			for x in range(1, width-1):
				print(board[y][x], end = " ")
			print("")




		#The choiceY and choiceX variables are not updating so the loop repetitively adds the same points to the list
			#choiceY and choiceX stay the same throughout the loop

			"""
			Solutions
			- Instead of value [choiceY + y] have position (1)
			- if (k==1) for first time and then elif (k==0) for second and adjust everything for position
			"""

	#-----------------------------------------------
	elif (field[choiceY][choiceX] != "B") and (field[choiceY][choiceX] != "0"): #also could put else instead of elif statement
		board[choiceY][choiceX] = field[choiceY][choiceX]

		for y in range (1, height-1):
			for x in range(1, width-1):
				print(board[y][x], end = " ")
			print("")
	#print board without any other point showing
#----------------------------------------------------------------
def flag():
	global flagX, flagY, flagC, flagW, height, width

	flagX = input("Give the x position you would like to flag: ")
	flagY = input("Give the y position you would like to flag: ")

	flagX = int(flagX)
	flagY = int(flagY)

	board[flagY][flagX] = "F"

	if (field[flagY][flagX] == "B"):
		flagC += 1

	else:
		flagW += 1

	for y in range (1, height-1):
			for x in range(1, width-1):
				print(board[y][x], end = " ")
			print("")

#----------------------------------------------------------------
def removeFlag():
	global removeX, removeY, flagW, flagC, height, width

	removeX = input("Give the x position you would like to remove the flag from: ")
	removeY = input("Give the y position you would like to remove the flag from: ")

	removeX = int(removeX)
	removeY = int(removeY)

	#Changing the count of correct flags
	if (board[flagY][flagX] == "F") and (field[flagY][flagX] == "B"):
		if (board[flagY][flagX] == board[removeY][removeX]):
			flagC -= 1

	#Changing the count of wrong flags
	if (board[flagY][flagX] == "F") and (field[flagY][flagX] != "B"):
		if (board[flagY][flagX] == board[removeY][removeX]):
			flagW -= 1

	#If the wrong point is chosen
	if (board[removeY][removeX] != "F"):
		print("You chose a point that wasn't flagged! Try again!")
		removeFlag()

	#if the point had a "#" before it was removed, put a "#" back in
	#if the point had a number before it was removed, put a number back in
	board[removeY][removeX] = "#"

	for y in range (1, height-1):
			for x in range(1, width-1):
				print(board[y][x], end = " ")
			print("")

#What about past points? Previously selected flagged values?
#----------------------------------------------------------------
def win():
	print("\n\nYou win!")

#----------------------------------------------------------------


#Game Setup
width = input("Width: ")
height = input("Height: ")
bombs = input("Bombs: ")

width = int(width)
height = int(height)
bombs = int(bombs)

width += 2
height += 2

#What player sees
board = []

board = [["#"]*width for x in range(height)]

#Solution
field = []

field = [["0"]*width for x in range(height)]


#Correct and wrong flags
flagC = int(0)
flagW = int(0)



#Makes the gutter all 1 so that there is no out of range problem
board[0] = [1]*width
board[-1] = [1]*width
for j in board:
	j[0] = 1
	j[-1] = 1



#Prints Board
for y in range (1, height-1):
	for x in range(1, width-1):
		print(board[y][x], end = " ")
	print("")

#Adds Bombs
count = 0
while (count < bombs):
	randomW = random.randint(1,width-2)
	randomH = random.randint(1,height-2)

	field[randomH][randomW] = "B"	

	count += 1

#Places Bombs and Adds Numbers
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

#--------------------------------------------------------------------------------------

#Game Start
playing = True

while (playing):

	if (flagC == bombs) and (flagW == 0):
		win()
		playing = False
		break


	choice = input("\nChoose your option:\n 1.) Reveal - Choose a spot on the board and reveal whether there is a bomb or not\n 2.) Flag - Mark a spot on the board where you think there is a bomb\n 3.) Remove Flag - Choose a flagged spot that you would like to remove the flag from\n\n Option: ")


	if (choice == "1") or (choice == "reveal")  or (choice == "Reveal"):
		reveal()

	if (choice == "2") or (choice == "flag") or (choice == "Flag"):
		flag()

	if (choice == "3") or (choice == "removeflag") or (choice == "remove flag") or (choice == "Remove flag") or (choice == "Remove Flag"):
		removeFlag()
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