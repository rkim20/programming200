#Initiation
from PIL import Image
from PIL import ImageFilter


#Functions


#Main

image = Image.open('program.jpg')
width, height = image.size

image.show()

for x in range (width):
	for y in range (height):
		r, g, b = image.getpixel((x,y))

		#image.putpixel((x,y),(r*2, g, b))
		image.putpixel((x,y), (0,g,0))


image = image.filter(ImageFilter.SHARPEN)
image.show()