#Initiation
from PIL import Image
from PIL import ImageFilter


#Functions


#Main--------------------------------------------------------------------

image = Image.open('filterphoto.jpg').convert('L')
width, height = image.size

image = image.filter(ImageFilter.SMOOTH_MORE)

image.show()

#-------------------------------------------------------------------------

image = Image.open('filterphoto.jpg')
width, height = image.size

for x in range (width):
	for y in range (height):
		r, g, b = image.getpixel((x,y))

		"""
		r = int(r*(50/100)) #43.9
		g = int(g*(50/100)) #25.9
		b = int(b*(35/100)) #7.8
		"""

		image.putpixel((x,y),(r*2, g, b))


#image = image.filter(ImageFilter.EMBOSS)

image.show()