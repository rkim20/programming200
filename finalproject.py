
#Initiation--------------------------------------------------------
from PIL import Image, ImageDraw
import random


#Functions--------------------------------------------------------- 

#Might have to switch x and y
def addFrontier(x, y):
	if (x == 0) and (y == 0):
		if (board[x+1][y] == "N"):
			frontier.append([x+1, y])
			board[x+1][y] = "F"
		if (board[x][y+1] == "N"):
			frontier.append([x, y+1])
			board[x][y+1] = "F"
	elif (x == 0) and (y == height-1):
		if (board[x+1][y] == "N"):
			frontier.append([x+1, y])
			board[x+1][y] = "F"
		if (board[x][y-1] == "N"):
			frontier.append([x, y-1])
			board[x][y-1] = "F"
	elif (x == width-1) and (y == 0):
		if (board[x-1][y] == "N"):
			frontier.append([x-1, y])
			board[x-1][y] = "F"
		if (board[x][y+1] == "N"):
			frontier.append([x, y+1])
			board[x][y+1] = "F"
	elif (x == width-1) and (y == height-1):
		if (board[x-1][y] == "N"):
			frontier.append([x-1, y])
			board[x-1][y] = "F"
		if (board[x][y-1] == "N"):
			frontier.append([x, y-1])
			board[x][y-1] = "F"

	elif (x == 0) and (y != 0) and (y != height-1):
		if (board[x+1][y] == "N"):
			frontier.append([x+1, y])
			board[x+1][y] = "F"
		if (board[x][y+1] == "N"):
			frontier.append([x, y+1])
			board[x][y+1] = "F"
		if (board[x][y-1] == "N"):
			frontier.append([x, y-1])
			board[x][y-1] = "F"
	elif (x == width-1) and (y != 0) and (y != height-1):
		if (board[x-1][y] == "N"):
			frontier.append([x-1, y])
			board[x-1][y] = "F"
		if (board[x][y+1] == "N"):
			frontier.append([x, y+1])
			board[x][y+1] = "F"
		if (board[x][y-1] == "N"):
			frontier.append([x, y-1])
			board[x][y-1] = "F"
	elif (y == 0) and (x != 0) and (x != width-1):
		if (board[x+1][y] == "N"):
			frontier.append([x+1, y])
			board[x+1][y] = "F"
		if (board[x-1][y] == "N"):
			frontier.append([x-1, y])
			board[x-1][y] = "F"
		if (board[x][y+1] == "N"):
			frontier.append([x, y+1])
			board[x][y+1] = "F"
	elif (y == height-1) and (x != 0) and (x != width-1):
		if (board[x+1][y] == "N"):
			frontier.append([x+1, y])
			board[x+1][y] = "F"
		if (board[x-1][y] == "N"):
			frontier.append([x-1, y])
			board[x-1][y] = "F"
		if (board[x][y-1] == "N"):
			frontier.append([x, y-1])
			board[x][y-1] = "F"
	elif (x != 0) and (x != width-1) and (y != 0) and (y != height-1): #also can do else
		if (board[x+1][y] == "N"):
			frontier.append([x+1, y])
			board[x+1][y] = "F"
		if (board[x-1][y] == "N"):
			frontier.append([x-1, y])
			board[x-1][y] = "F"
		if (board[x][y+1] == "N"):
			frontier.append([x, y+1])
			board[x][y+1] = "F"
		if (board[x][y-1] == "N"):
			frontier.append([x, y-1])
			board[x][y-1] = "F"
		
def removeLines(point1, point2):
	#point1 = 0,3
	#point2 = 1,3
	if (point1[0] + 1 == point2[0]) or (point1[0] - 1 == point2[0]):
		#Same but changes depending on whether the x value of point1 or point2 is greater
		if (point1[0] < point2[0]):
			draw.line(((imgx/width) * point2[0],(imgy/height) * point1[1], (imgx/width) * point2[0],(imgy/height) * (point1[1]+1)), fill = 0, width = 3)
		else:
			draw.line(((imgx/width) * point1[0],(imgy/height) * point1[1], (imgx/width) * point1[0],(imgy/height) * (point1[1]+1)), fill = 0, width = 3)
			#imgx/width * point2[0], imgy/height * point1[1], imgx/width * point2[0], imgy/height * point1[1]+1

	#point1 = 1, 2
	#point2 = 1, 3
	elif (point1[1] + 1 == point2[1]) or (point1[1] - 1 == point2[1]):
		if (point1[1] < point2[1]):
			draw.line(((imgx/width) * point1[0],(imgy/height) * point2[1], (imgx/width) * (point1[0]+1),(imgy/height) * point2[1]), fill = 0, width = 3)
		elif (point1[1] > point2[1]):
			draw.line(((imgx/width) * point1[0],(imgy/height) * point1[1], (imgx/width) * (point1[0]+1),(imgy/height) * point1[1]), fill = 0, width = 3)
			#imgx/width * point1[0], imgy/height * point2[1], imgx/width * point1[0]+1, imgy/height * point2[1]

#Create a function or add to this one that goes through every pixel and checks to see if it is surrounded by red or black to add red points to the edges
#Main--------------------------------------------------------------
#ADD ERROR CHECKING
width = input("Input the width of the maze: ")
height = input("Input the height of the maze: ")

width = int(width)
height = int(height)

imgx = 500
imgy = 500

image = Image.new("RGB",(imgx,imgy))
draw = ImageDraw.Draw(image)

for x in range (1,width):
	draw.line(((imgx/width)*x,0, (imgx/width)*x,imgy), fill = 255, width = 3)

for y in range (1,height):
	draw.line((0,(imgy/height)*y, imgx, (imgy/height)*y), fill = 255, width = 3)


#Board Setup - top left is (0,0)
board = []
board = [["N"]*width for x in range(height)]

visited = []
frontier = []

"""
for x in range(width):
	for y in range(height):
		board[y][x] = x, y
"""

startX = random.randint(0,width)
startY = random.randint(0,height)
startV = startX, startY

#Maze starts
visited.append([startX, startY])
board[startY][startX] = "V"
"""
visited[0] = startX, startY
visited[0,0] = startX
visited[0,1] = startY
"""

addFrontier(startX, startY)


while (len(frontier) > 0):
	count = 0

	newV = random.randint(0, len(frontier))
	visited.append(frontier[newV])
	board[frontier[newV][0]][frontier[newV][1]] = "V"

	a, b = frontier[newV]
	updatedV = a, b

	addFrontier(a, b)

	del frontier[newV]

	#Function for erasing the lines
	if (count == 1):
		removeLines(startV, updatedV)
		count++
	else:
		#Create a function that is made of if statements and checks to see how many V points are around the given point before providing a random V point (maybe returns it) - this will provide the updatedV point another point that has already been deemed "V" and remove the lines between them
		removeLines(updatedV, )

image.show()





#At the end, write why I did or didn't use a class