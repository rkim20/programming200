#Initiation
from PIL import Image
from PIL import ImageFilter
import colorsys


#Functions


#Main--------------------------------------------------------------------

image = Image.open('photo2.jpg').convert('L')
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

#-------------------------------------------------------------------------
"""
image  = Image.open('photo3.jpg')
width, height = image.size

for x in range (width):
	for y in range (height):
		r, g, b = image.getpixel((x,y))

		r = int(r/255)
		g = int(g/255)
		b = int(b/255)

		h, s, v = colorsys.rgb_to_hsv(r,g,b)

		h = int(h*255)
		s = int(s*100)
		v = int(v*100)

		if (s <= 60):
			s += 20

		h = h/255
		s = s/100
		v = v/100

		r, g, b = colorsys.hsv_to_rgb(h,s,v)

		r = int(r*255)
		g = int(g*255)
		b = int(b*255)

		image.putpixel((x,y), (r,g,b))


image.show()
"""










