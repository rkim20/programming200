from PIL import Image
import colorsys
import random

#Size of image
imgx, imgy = 512, 512

#Number of iterations
maxIt = 256

image = Image.new("RGB", (imgx, imgy))


#minimum and maximum range of z vallue
x1, x2 = -2.0, 2.0
y1, y2 = -2.0, 2.0

image = Image.new("RGB", (imgx, imgy))


#Sets up pixel grid
for y in range(imgy):

	#splits y pixels into number that fits in the range of c
	cy = y*(y2-y1) / (imgy-1) + y1


	for x in range(imgx):

		#splits x pixels into number that fits in the range of c
		cx = x*(x2-x1) / (imgx-1) + x1

		c = complex(-0.8,0.156) #treats value like a complex number
		z = complex(cx, cy)

		#Goes through breaking out process with each point
		for i in range(maxIt):
			if (abs(z) >= 2.0):
				break
			z = z**2 + c


		r = i%256
		g = i+40
		b = i*2

		image.putpixel((x,y),(r,g,b))


image.show()







