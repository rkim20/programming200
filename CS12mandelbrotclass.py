#Ryan Kim
#Date
#Honor Code
#Explanation
"""
Colorsys - https://docs.python.org/2/library/colorsys.html
- I used this source to help me understand and utilize the colorsys tool. This helped me use HSV color values in my first and second image instead of RGB values.

Filters - https://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
- I used this source to get a list of the filters I could use to enhance and change my images.

Filters - https://www.youtube.com/watch?v=06bDaMGd-zQ
- I used this source to understand and see what the filters would do. It gave me a general idea of what each filter did while also giving me the list of the different filters.

Invert Colors - https://www.youtube.com/watch?v=MVLuexuikv4
- I used this source to get an idea on how to invert the colors. There was a lot of information, but I focused mostly on the inverted colors which I used in my first and last image.
"""
#---------------------------------------------------------------------------------------------------

from PIL import Image
from PIL import ImageFilter
import PIL.ImageOps
import colorsys

#---------------------------------------------------------------------------------------------------
#First Image - Mandelbrot set

#Minimum and maximum range of c value
xa, xb = -1.586, -1.539
ya, yb = -0.02284, 0.02371

#Size of image
imgx, imgy = 512, 512

#Number of iterations
maxIt = 256

image = Image.new("RGB", (imgx, imgy))

#Sets up pixel grid
for y in range(imgy):

	cy = y*(yb-ya) / (imgy-1) + ya

	for x in range(imgx):
		cx = x*(xb-xa) / (imgx-1) + xa

		c = complex(cx,cy)
		z = 0

		for i in range(maxIt):
			if (abs(z) >= 2.0):
				break
			z = z**2 + c

		#HSV colors values are changed to RGB values and then used - allows me to input HSV color values

		#Lets me put in values like RGB instead of between 0 and 1
		h = ((i*2)%50)-10 #range is 255
		s = (i%5)+95 #range is 100
		v = (i%20)+80 #range is 100

		#Changes the values I input into values between 0-1 which are the allowed HSV values
		h = h/255
		s = s/100
		v = v/100

		#Conversion function
		r, g, b = colorsys.hsv_to_rgb(h,s,v)

		#Multiplies to fit into RGB scale which is not 0-1 but 0-255
		r = int(r*255)
		g = int(g*255)
		b = int(b*255)
		
		image.putpixel((x,y),(r,g,b))

#Inverts image colors
inverted_image = PIL.ImageOps.invert(image)
inverted_image.show()
#---------------------------------------------------------------------------------------------------
#Second Image - Julia Set (julia set is the same except c changes and z stays the same)

x1, x2 = 0.15, 0.80
y1, y2 = -0.40, 0.25

image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):

	cy = y*(y2-y1) / (imgy-1) + y1

	for x in range(imgx):
		cx = x*(x2-x1) / (imgx-1) + x1

		c = complex(-0.75,0.156)
		z = complex(cx, cy)

		for i in range(maxIt):
			if (abs(z) >= 2.0):
				break
			z = z**2 + c

		#HSV colors values are changed to RGB values and then used - allows me to input HSV color values

		#Lets me put in values like RGB
		h = ((i%50)+170) #range is 255
		s = (i%20)+80 #range is 100
		v = (i%20)+80 #range is 100

		#Changes the values I input into values between 0-1 which are the allowed HSV values
		h = h/255
		s = s/100
		v = v/100

		r, g, b = colorsys.hsv_to_rgb(h,s,v)

		#Multiplies to fit into RGB scale which is not 0-1 but 0-255
		r = int(r*255)
		g = int(g*255)
		b = int(b*255)

		image.putpixel((x,y),(r,g,b))

image.show()
#---------------------------------------------------------------------------------------------------
#Third Image - Mandelbrot Set

xa, xb = 0.3377, 0.3558
ya, yb = 0.3751, 0.3933

image = Image.new("RGB", (imgx, imgy))

for y in range(imgy):

	cy = y*(yb-ya) / (imgy-1) + ya

	for x in range(imgx):
		cx = x*(xb-xa) / (imgx-1) + xa

		c = complex(cx,cy)
		z = 0

		for i in range(maxIt):
			if (abs(z) >= 2.0):
				break
			z = z**2 + c
		
		r = i*2
		g = i%256
		b = i+20

		image.putpixel((x,y),(r,g,b))

#Inverts the colors
inverted_image = PIL.ImageOps.invert(image)
image = inverted_image

#Adds a filter to the image - creates a blurry-type image
image.filter(ImageFilter.SMOOTH).show()




"""
- Go over general comments again
- Ask about adding extra comments regarding Julia set - do I have to explain what I did or can I assume you know?
- Ask about using filters in more than just last image - if it's okay to only use it in one or if it would be better to use in many
"""









