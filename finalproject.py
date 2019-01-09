"""
Ryan Kim
Date: Thursday, November 15th, 2018
Honor Code: On my honor, I have neither given nor received unauthorized aid.

Sources:
http://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm
- I used this source to help get a better understanding of Prim's algorithm. I frequently used it to design my code around the same idea

https://stackoverflow.com/questions/33240374/how-can-draw-a-line-using-the-x-and-y-coordinates-of-two-points
- I used this source to understand how to draw lines in images using PIL.

https://docs.python.org/3/tutorial/datastructures.html
- I used this source to get a better understanding of the pop, remove, and del functions as I got confused with their differences are various times throughout my project.

https://stackoverflow.com/questions/41405632/draw-a-rectangle-and-a-text-in-it-using-pil
- I used this source to help me understand how to draw a rectangle in an image using PIL.

Description: For my final project, I decided to learn about Prim's algorithm and use it to create a maze. There were many different ways to go about this project and many areas in which I could have chosen a different path towards achieving the same goal. For example, the maze could have been designed as a text based maze, meaning it would print in Terminal rather than as an image. I wanted to display the maze on an image because I thought I could add extra details and elements that couldn't be accessed in a text based maze. Additionally, the visual appeal of it would be much better on an image rather than as a text based maze. Adding onto this idea of different methods, I purposefully chose not to use classes because I felt that it would only hinder my code. When my original plan for the maze came into my head, I saw everything I needed to do and didn't see the need for classes. I thought it might make things a bit more organized but would overall make things over complicated. I decided that I coudl easily go about the maze without creating any classes. I also saw this multitude of paths when dealing with some of my longer functions. There were a number of different parameters in the if statements that I could have used, and I tried to find the most efficient way to do what I wanted. However, these functions which included the addFrontier() function and the checkV() function still turned out extremely long because of all the possibilities they had to include. They had to make sure they could run if the values they got were in the corner of the grid or on a wall. This extended the code and made it extremely tedious, especially when checking for errors. This was one of the main challenges I had. Even though the code was generally easy to understand, one wrong bracket or switched x and y value could have the entire maze not working. There were many times where I struggled to find the problems in my code for this precise reason, and it had me extremely frustrated. One of the more minor problems that I faced during this project was simply understanding basic lines of code. I would forget whether random.randint() was inclusive on both ends or what the exact differences between pop, remove, and del were. These also made my work tedious because I would think I knew what they did, but these mistakes in my knowledge would result in my code not working. Overall, though there were some rough spots, I really enjoyed this project. There was some sort of satisfaction whenever I got another part of my maze working and seeing the entire thing complete really gave me happiness. In terms of feedback from friends, I started out with my start and end points as lines on one of the four walls. They suggested I, instead, do different points at random locations within the maze. I decided to look into this and found that I preferred this choice as well. In addition to that, I initially had the width and length set up to be what the user wanted. However, I was inspired by a Minesweeper app that I downloaded where there are different levels as well as an option for a custom grid. I applied this to my own code, providing different levels as well as an option for a custom grid. I also wanted to add another aspect of fun to my maze. I felt like a simple maze would get too boring, even if the grid could be increased. I decided to add the challenge boxes or gems. This way, the user could increase the number of challenge boxes and this would increase the level of difficulty to as much as the user wanted. Finally, I initially designed the maze so that where a line was removed, the red lines around it aren't perfectly connected. I started to make a function that would change this, but after seeing the maze in its higher widths and heights, I felt that I preferred the current design aesthetically and decided to keep it that way. Overall, this was a tough project, and I had to face frustrating challenges, but I enjoyed the entire thing. 

"""


#Imports-----------------------------------------------------------
from PIL import Image, ImageDraw
import random


#Functions--------------------------------------------------------- 
#This function contains the code for the start of the game, allowing the user to select their level. I used a function here to be able to call on it as many times as possible if the user was unable to inpute the correct values for the code to run.

def start():
	global width, height, gems

	print("\nLevels\n 1.) Easy (5x5)\n 2.) Medium (10x10)\n 3.) Hard (15x15)\n 4.) Custom")

	level = input("\nPlease select your level by typing the number or writing the difficulty: ")

	if (level == "1") or (level == "easy") or (level == "Easy") or (level == "E") or (level == "e"):
		width = 5
		height = 5
		gems = 0
	elif (level == "2") or (level == "medium") or (level == "Medium") or (level == "M") or (level == "m"):
		width = 10
		height = 10
		gems = 1
	elif (level == "3") or (level == "hard") or (level == "Hard") or (level == "H") or (level == "h"):
		width = 15
		height = 15
		gems = 2
	elif (level == "4") or (level == "custom") or (level == "Custom") or (level == "C") or (level == "c"):
		while True:
			try:
				width = input("Input the width of the maze: ")
				height = input("Input the height of the maze: ")
				gems = input("Input the number of challenge boxes in your maze: ")
				width = int(width)
				height = int(height)
				gems = int(gems)
				if (width > 40) or (height > 40) or (gems > 40):
					print("\n----------------------------------------\nYou didn't input the correct values to pick your level. Please try again.")
					start()
				break
			except ValueError:
					print("\n----------------------------------------\nYou didn't input the correct values to pick your level. Please try again.")
	else:
		print("\n----------------------------------------\nYou didn't input the correct values to pick your level. Please try again.")
		start()

#-------------------------------------------------------------------------------------------------------------------
#This function adds the frontier points in Prim's Algorithm. It receives two values, the a and b (x,y) values of the visited point and adds all the points around it (not including diagonal) to the frontier list. There were multiple ways to go about adding the frontier points, and I struggled with finding the best way. In the end, because I had used a list similar to that in the minesweeper game to show which points were visited (V), which were frontier (F), and which were not yet marked (N), I used this to my advantage and applied it to my code when adding the frontier points. I used it in the if statements to see whether or not the surrounding points were already marked as "V" or "F". If not, the code would go on to add that point to the frontier list.

def addFrontier(x, y):
	if (x == 0) and (y == 0):
		if (board[y+1][x] == "N"):
			frontier.append([x, y+1])
			board[y+1][x] = "F"
		if (board[y][x+1] == "N"):
			frontier.append([x+1, y])
			board[y][x+1] = "F"
	elif (x == 0) and (y == height-1):
		if (board[y-1][x] == "N"):
			frontier.append([x, y-1])
			board[y-1][x] = "F"
		if (board[y][x+1] == "N"):
			frontier.append([x+1, y])
			board[y][x+1] = "F"
	elif (x == width-1) and (y == 0):
		if (board[y+1][x] == "N"):
			frontier.append([x, y+1])
			board[y+1][x] = "F"
		if (board[y][x-1] == "N"):
			frontier.append([x-1, y])
			board[y][x-1] = "F"
	elif (x == width-1) and (y == height-1):
		if (board[y-1][x] == "N"):
			frontier.append([x, y-1])
			board[y-1][x] = "F"
		if (board[y][x-1] == "N"):
			frontier.append([x-1, y])
			board[y][x-1] = "F"

	elif (x == 0):
		if (board[y+1][x] == "N"):
			frontier.append([x, y+1])
			board[y+1][x] = "F"
		if (board[y][x+1] == "N"):
			frontier.append([x+1, y])
			board[y][x+1] = "F"
		if (board[y-1][x] == "N"):
			frontier.append([x, y-1])
			board[y-1][x] = "F"
	elif (x == width-1):
		if (board[y-1][x] == "N"):
			frontier.append([x, y-1])
			board[y-1][x] = "F"
		if (board[y][x-1] == "N"):
			frontier.append([x-1, y])
			board[y][x-1] = "F"
		if (board[y+1][x] == "N"):
			frontier.append([x, y+1])
			board[y+1][x] = "F"
	elif (y == 0):
		if (board[y+1][x] == "N"):
			frontier.append([x, y+1])
			board[y+1][x] = "F"
		if (board[y][x+1] == "N"):
			frontier.append([x+1, y])
			board[y][x+1] = "F"
		if (board[y][x-1] == "N"):
			frontier.append([x-1, y])
			board[y][x-1] = "F"
	elif (y == height-1):
		if (board[y-1][x] == "N"):
			frontier.append([x, y-1])
			board[y-1][x] = "F"
		if (board[y][x+1] == "N"):
			frontier.append([x+1, y])
			board[y][x+1] = "F"
		if (board[y][x-1] == "N"):
			frontier.append([x-1, y])
			board[y][x-1] = "F"
	elif (x > 0) and (x < width-1) and (y > 0) and (y < height-1):
		if (board[y+1][x] == "N"):
			frontier.append([x, y+1])
			board[y+1][x] = "F"
		if (board[y-1][x] == "N"):
			frontier.append([x, y-1])
			board[y-1][x] = "F"
		if (board[y][x+1] == "N"):
			frontier.append([x+1, y])
			board[y][x+1] = "F"
		if (board[y][x-1] == "N"):
			frontier.append([x-1, y])
			board[y][x-1] = "F"
		
#-------------------------------------------------------------------------------------------------------------------
#I created this function to remove the lines between two visited points. I thought the best way to "remove" these lines would be to simply draw over them with the background color which in this case was black. I found the draw.line function and did the math so that part of the original grid would be drawn over. The two outermost if statements are used to see if the line being removed is horizontal or vertical. As the code would be different depending on whether the line was drawn upwards or sideways, these if statements simply broke the line drawing into two categories. Within these if statements, I used a series of math sets that would allow the line to be removed in all widths and heights and not just a specific set.

def removeLines(point1, point2):

	if (point1[0] + 1 == point2[0]) or (point1[0] - 1 == point2[0]):
		#Code is same but changes depending on whether the x value of point1 or point2 is greater
		if (point1[0] < point2[0]):
			draw.line(((imgx/width) * point2[0],(imgy/height) * point1[1], (imgx/width) * point2[0],(imgy/height) * (point1[1]+1)), fill = 0, width = 3)
		else:
			draw.line(((imgx/width) * point1[0],(imgy/height) * point1[1], (imgx/width) * point1[0],(imgy/height) * (point1[1]+1)), fill = 0, width = 3)

	elif (point1[1] + 1 == point2[1]) or (point1[1] - 1 == point2[1]):
		if (point1[1] < point2[1]):
			draw.line(((imgx/width) * point1[0],(imgy/height) * point2[1], (imgx/width) * (point1[0]+1),(imgy/height) * point2[1]), fill = 0, width = 3)
		elif (point1[1] > point2[1]):
			draw.line(((imgx/width) * point1[0],(imgy/height) * point1[1], (imgx/width) * (point1[0]+1),(imgy/height) * point1[1]), fill = 0, width = 3)

#-------------------------------------------------------------------------------------------------------------------
#I created this function when choosing which line to get rid of. Sometimes, the newest visited point could have several options for removing lines as it could be surrounded by multiple visited points. This function helped check to see how many visited points were surrounding the given point received in a,b and then would randomly select one of these points and return it. This returned point would be inserted into the removeLines() function with the newest visited point already in the first argument. One of the main struggles in this code was that I had to have parameters for every single a,b case. If a,b was in the corner, it had a different code to run than if it was on the side or in the middle. This extended the code by a lot and gave room for much more errors to occur.
#a,b - updatedV value (newest visited point)
#c,d - holds the values of the possibleV values that are used to check whether the points around a,b are visited points

def checkV(a,b):
	global possibleV

	possibleV = [[-1,0],[1,0],[0,-1],[0,1]]

	if (a > 0) and (a < width-1) and (b > 0) and (b < height-1):
		random.shuffle(possibleV)
		while (len(possibleV) > 0):
			c = possibleV[0][0]
			d = possibleV[0][1]
			if ([a+c,b+d] in visited):
				return (a+c,b+d)
			else:
				possibleV.pop(0)

	elif (a == 0) and (b == 0):

		#These two values are popped because they are out of the range since the point a,b is in the corner - they are also in this specific order because popping the first value would change what the third value was
		possibleV.pop(2)
		possibleV.pop(0)

		random.shuffle(possibleV) #The list is shuffled so that which point is first checked is always random

		while (len(possibleV) > 0):
			c = possibleV[0][0]
			d = possibleV[0][1]
			if ([a+c,b+d] in visited):
				return (a+c,b+d)
			else:
				possibleV.pop(0)
				#If the code reaches this point, it means that one of the surrounding points of a,b isn't a visited point and therefore is popped

	elif (a == 0) and (b == height-1):
		possibleV.pop(3)
		possibleV.pop(0)
		random.shuffle(possibleV)
		while (len(possibleV) > 0):
			c = possibleV[0][0]
			d = possibleV[0][1]
			if ([a+c,b+d] in visited):
				return (a+c,b+d)
			else:
				possibleV.pop(0)

	elif (a == width-1) and (b == 0):
		possibleV.pop(2)
		possibleV.pop(1)
		random.shuffle(possibleV)
		while (len(possibleV) > 0):
			c = possibleV[0][0]
			d = possibleV[0][1]
			if ([a+c,b+d] in visited):
				return (a+c,b+d)
			else:
				possibleV.pop(0)

	elif (a == width-1) and (b == height-1):
		possibleV.pop(3)
		possibleV.pop(1)
		random.shuffle(possibleV)
		while (len(possibleV) > 0):
			c = possibleV[0][0]
			d = possibleV[0][1]
			if ([a+c,b+d] in visited):
				return (a+c,b+d)
			else:
				possibleV.pop(0)

	elif (a == 0):
		possibleV.pop(0)
		random.shuffle(possibleV)
		while (len(possibleV) > 0):
			c = possibleV[0][0]
			d = possibleV[0][1]
			if ([a+c,b+d] in visited):
				return (a+c,b+d)
			else:
				possibleV.pop(0)

	elif (a == width-1):
		possibleV.pop(1)
		random.shuffle(possibleV)
		while (len(possibleV) > 0):
			c = possibleV[0][0]
			d = possibleV[0][1]
			if ([a+c,b+d] in visited):
				return (a+c,b+d)
			else:
				possibleV.pop(0)

	elif (b == 0):
		possibleV.pop(2)
		random.shuffle(possibleV)
		while (len(possibleV) > 0):
			c = possibleV[0][0]
			d = possibleV[0][1]
			if ([a+c,b+d] in visited):
				return (a+c,b+d)
			else:
				possibleV.pop(0)

	elif (b == height-1):
		possibleV.pop(3)
		random.shuffle(possibleV)
		while (len(possibleV) > 0):
			c = possibleV[0][0]
			d = possibleV[0][1]
			if ([a+c,b+d] in visited):
				return (a+c,b+d)
			else:
				possibleV.pop(0)

#-------------------------------------------------------------------------------------------------------------------
#I created this function to make and set the starting point for the maze. I was going to have the start and ends points be some place on the walls, but I decided to mix it up and have the starts and ends be at different points throughout the maze itself. Initially, I had both the start and end points in the same function. However, I didn't want the points to overlap, so I created a different function for the end point. In this start function, I had to research to find the functions for a rectangle. After that, I did the math to find the right parameters for the rectangle to fit perfectly within one of the square grids. I also made sure the algorithm I designed could be applied to any and all widths and heights.

def startPoint():
	global xPoint, yPoint

	draw.rectangle( ( ( ((imgx/width)*xPoint) + int((imgx/width)*(1/3)), ((imgy/height)*yPoint) + int((imgy/height)*(1/3)) ), ((imgx/width)*xPoint) + int((imgx/width)*(2/3)), ((imgy/height)*yPoint) + int((imgy/height)*(2/3)) ), fill="green", outline = "green")

#-------------------------------------------------------------------------------------------------------------------
#This function is pretty much the same as the startPoint() function other than that this one has steps to ensure that the two lines don't overlap. The xPoint, yPoint, xEndPoint, and yEndPoint basically guide the locations of the start and end lines, so the if statement makes it so that until they are different from each other, the end point will not be drawn.

def endPoint():
	global xPoint, yPoint

	xPointEnd = random.randint(0,width-1) #Gives the x location of the end point
	yPointEnd = random.randint(0,height-1) #Gives the y location of the end point

	if (xPointEnd == xPoint) or (yPointEnd == yPoint):
		endPoint()

	else:
		draw.rectangle( ( ( ((imgx/width)*xPointEnd) + int((imgx/width)*(1/3)), ((imgy/height)*yPointEnd) + int((imgy/height)*(1/3)) ), ((imgx/width)*xPointEnd) + int((imgx/width)*(2/3)), ((imgy/height)*yPointEnd) + int((imgy/height)*(2/3)) ), fill="blue", outline = "blue")

#-------------------------------------------------------------------------------------------------------------------
#This function was an added level of fun to the maze. It provided a white box in one of the grid squares and acted as an extra challenge. Although it doesn't really affect much in the easier levels, it does make the maze harder in the more advanced levels as it essentially provides the user with two different goals. In terms of code, I used the code for the start and end points.

def gem():
	locationX = random.randint(0,width-1) #Gives the x location of the rectangle
	locationY = random.randint(0,height-1) #Gives the y location of the reactangle

	draw.rectangle( ( ( ((imgx/width)*locationX) + int((imgx/width)*(1/3)), ((imgy/height)*locationY) + int((imgy/height)*(1/3)) ), ((imgx/width)*locationX) + int((imgx/width)*(2/3)), ((imgy/height)*locationY) + int((imgy/height)*(2/3)) ), fill="white", outline = "white")

#Main--------------------------------------------------------------

#Initiation--------------------------------------------------------

width = 0
height = 0
gems = 0

print("\n------------------------------------------------\nWelcome to The Maze!\n\nThe start of the maze is marked by the green square and the end of the maze is marked by the blue square.\n\nFind your way from the green square to the blue one to win.\n\nIf you believe yourself smart enough, try to reach the white box before going to the end point.\n\nALERT: DON'T SET YOUR WIDTH, HEIGHT, OR CHALLENGE BOXES GREATER THAN 40!")

start()

width = int(width)
height = int(height)

imgx = 500
imgy = 500

image = Image.new("RGB",(imgx,imgy))
draw = ImageDraw.Draw(image)


#Draws the original grid
for x in range (1,width):
	draw.line(((imgx/width)*x,0, (imgx/width)*x,imgy), fill = 255, width = 3)

for y in range (1,height):
	draw.line((0,(imgy/height)*y, imgx, (imgy/height)*y), fill = 255, width = 3)


#Board Setup - top left is (0,0) - The board was originally meant for my own personal understanding, but later came to help with my functions in terms of having the "F" and "N" plotted out
board = []
board = [["N"]*width for x in range(height)]

#Lists I used
visited = [] #visited list
frontier = [] #frontier list
possibleV = [] #list for possible visited points that might have its wall removed

#Starting visited points
startX = random.randint(0,width-1)
startY = random.randint(0,height-1)
startV = startX, startY

#For start/end functions - added outside so can be accessed by end() through global
xPoint = random.randint(0,width-1) #Gives the x location of the start point
yPoint = random.randint(0,height-1) #Gives the y location of the start point

#Prim's Algorithm Starts---------------------------------------------------------------
"""
Variables/Explanation
- count: Divides the code into the first time going through and every other time after that. The first time, the removeLines() function holds the startV and the updatedV no matter what. After that, however, the removeLines() function holds different values each time it goes through the code. The count variable simply changes the code that will run after it goes through once.
- newV: This is a random number within the length of the frontier list. It is used to randomly add one of the frontier points to the visited list and then that frontier point is removed.
- updatedV/a,b - Essentially they are the same thing just split into two values in a,b. The frontier[newV] is put into them so that the values can be used even after the frontier[newV] is deleted. Their primary use is in the removelines() function as they are the most recently added visited point and therefore must have their wall between another visited point be removed.
"""

visited.append([startX, startY])

addFrontier(startX, startY)

count = 0

#Keeps Prim's algorithm running until the maze is complete
while (len(frontier) > 0):

	#Random point from the frontier list to moved to the visited list - essentially, a frontier point turns into a visited point
	newV = random.randint(0, len(frontier)-1)
	visited.append(frontier[newV])

	a, b = frontier[newV]
	updatedV = a, b

	addFrontier(a, b)

	del frontier[newV]

	#Erasing lines
	if (count == 0): #Only for the first time
		removeLines(startV, updatedV)
		count+=1
	else: #Everytime after the first time
		newestV = checkV(a,b)
		removeLines(updatedV, newestV)

#Final Drawing-------------------------------------------------------------------------

startPoint()
endPoint()
for x in range(gems):
	gem()

image.show()