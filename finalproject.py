
#Initiation--------------------------------------------------------
from PIL import Image, ImageDraw
import random


#Functions---------------------------------------------------------



#Main--------------------------------------------------------------
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
		board[x][y] = x, y
"""

startX = random.randint(0,width)
startY = random.randint(0,height)

#Maze starts
visited.append([startX, startY])
"""
visited[0] = startX, startY
visited[0,0] = startX
visited[0.1] = startY
"""


if (startX == 0):
	frontier.append([startX+1, startY])
	frontier.append([startX, startY+1])
	frontier.append([startX, startY-1])
	board[startX+1][startY] = "F"
	board[startX][startY+1] = "F"
	board[startX][startY-1] = "F"
elif (startX == width-1):
	frontier.append([startX-1, startY])
	frontier.append([startX, startY+1])
	frontier.append([startX, startY-1])
	board[startX-1][startY] = "F"
	board[startX][startY+1] = "F"
	board[startX][startY-1] = "F"
elif (startY == 0):
	frontier.append([startX+1, startY])
	frontier.append([startX-1, startY])
	frontier.append([startX, startY+1])
	board[startX+1][startY] = "F"
	board[startX-1][startY] = "F"
	board[startX][startY+1] = "F"
elif (startY == height-1):
	frontier.append([startX+1, startY])
	frontier.append([startX-1, startY])
	frontier.append([startX, startY-1])
	board[startX+1][startY] = "F"
	board[startX-1][startY] = "F"
	board[startX][startY-1] = "F"
else:
	frontier.append([startX+1, startY])
	frontier.append([startX-1, startY])
	frontier.append([startX, startY+1])
	frontier.append([startX, startY-1])
	board[startX+1][startY] = "F"
	board[startX-1][startY] = "F"
	board[startX][startY+1] = "F"
	board[startX][startY-1] = "F"


while (len(frontier) > 0):
	newV = random.randint(len(frontier))
	frontier[newV] = 



image.show()





#At the end, write why I did or didn't use a class