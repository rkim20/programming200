from PIL import Image
import colorsys
import random

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

	#splits pixels into number that fits in the range of c
	cy = y*(yb-ya) / (imgy-1) + ya


	for x in range(imgx):
		cx = x*(xb-xa) / (imgx-1) + xa

		c = complex(cx,cy) #treats value like a complex number
		z = 0

		#Goes through breaking out process with each point
		for i in range(maxIt):
			if (abs(z) >= 2.0):
				break
			z = z**2 + c

		"""
		Colors
		- color is limited to 255 so must adjust the maxIt or the rgb to change color (rgb)
		- multiplying - creates the color blocks
		- dividing - makes color change smoother
		- adding/subtracting - moves range/domain
		"""

		#HSV colors values are changed to RGB values and then used - allows me to input HSV color values

		color = random.randint(0,255)

		#Lets me put in values like RGB
		h = ((i*2)%50)-10 #range is 255
		#^instead of -10, 130, 170 are good too
		s = (i%5)+95 #range is 100
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


#image.show()
#---------------------------------------------------------------------------------------------------
#Second Image - Julia Set (julia set is the same except c changes and z stays the same)

#minimum and maximum range of z vallue
x1, x2 = 0.05, 0.90
y1, y2 = -0.45, 0.40

image = Image.new("RGB", (imgx, imgy))


#Sets up pixel grid
for y in range(imgy):

	#splits y pixels into number that fits in the range of c
	cy = y*(y2-y1) / (imgy-1) + y1


	for x in range(imgx):

		#splits x pixels into number that fits in the range of c
		cx = x*(x2-x1) / (imgx-1) + x1

		c = complex(-0.75,0.156) #treats value like a complex number
		z = complex(cx, cy)

		#Goes through breaking out process with each point
		for i in range(maxIt):
			if (abs(z) >= 2.0):
				break
			z = z**2 + c


		r = i%256
		g = i
		b = i+20

		image.putpixel((x,y),(r,g,b))


image.show()












