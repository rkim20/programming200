
#Initiation--------------------------------------------------------
from PIL import Image, ImageDraw


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

draw.line((imgx/width,0, imgx/width,imgy), fill = 255, width = 3)


image.show()