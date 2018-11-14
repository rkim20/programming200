
#Initiation--------------------------------------------------------
from PIL import Image, ImageDraw
import random


#Functions--------------------------------------------------------- 

#Might have to switch x and y
#Adds 

#Problem - frontier x and y values are switched
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


def checkV(a,b):
	global possibleV
	#----------------
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
		possibleV.pop(2)
		possibleV.pop(0)
		random.shuffle(possibleV)
		while (len(possibleV) > 0):
			c = possibleV[0][0]
			d = possibleV[0][1]
			if ([a+c,b+d] in visited):
				return (a+c,b+d)
			else:
				possibleV.pop(0)

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


def checkPixels():
	for x in range(1,imgx-1):
		for y in range(1,imgy-1):
			r, g, b = image.getpixel((x,y))
			if (r == 0):
				newR,newG,newB = image.getpixel
	#Help - try and find a way to do this more easily - getting info of pixel
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
possibleV = []

"""
for x in range(width):
	for y in range(height):
		board[y][x] = x, y
"""

#--------------
# is randint inclusive of second value?
#--------------
startX = random.randint(0,width-1)
startY = random.randint(0,height-1)
startV = startX, startY
print(startV)

#Maze starts

visited.append([startX, startY])
board[startY][startX] = "V"
"""
visited[0] = startX, startY
visited[0,0] = startX
visited[0,1] = startY
"""

addFrontier(startX, startY)

count = 0
while (len(frontier) > 0):

	newV = random.randint(0, len(frontier)-1)
	visited.append(frontier[newV])
	print(frontier[newV])
	board[frontier[newV][0]][frontier[newV][1]] = "V"

	a, b = frontier[newV]
	updatedV = a, b

	addFrontier(a, b)

	del frontier[newV]

	#Function for erasing the lines
	if (count == 0):
		removeLines(startV, updatedV)
		count+=1
	else:
		print("A and B: " + str(a),str(b))
		newestV = checkV(a,b)
		print("Check V: " + str(newestV))
		print("Updated V: " + str(updatedV))
		print("-----")
		removeLines(updatedV, newestV)

image.show()





#At the end, write why I did or didn't use a class
#Creative - add levels and then custom