from PIL import Image
import colorsys

#Minimum and maximum range of c value
xa, xb = 0, 0.05
ya, yb = 0.80, 0.87

#Size of image
imgx, imgy = 512, 512

#Number of iterations
maxIt = 256

image = Image.new("RGB", (imgx, imgy))

#Sets up image grid
for y in range(imgy):
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
		- color is limited to 255 so must adjust the maxIt or the rgb to change color
		- multiplying - creates the color blocks
		- dividing - makes color change smoother
		- adding/subtracting - moves range/domain
		"""

		#HSV colors values are changed to RGB values and then used - allows me to input HSV color values

		h = 239
		s = 90
		v = 77

		r, g, b = colorsys.hsv_to_rgb(h,s,v)

		r = int(r)
		g = int(g)
		b = int(b)
		
		image.putpixel((x,y),(r,g,b))


image.show()








