"""
Ryan Kim
HW for Monday, October 15th

Sources: http://colorizer.org/ - I used this source to get the values of colors in the RGB mode
"""


from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx,imgy))

c = int(255)

for x in range(512):
	for y in range(512):
		image.putpixel((x,y),(c,0,0))

		c -= 1
		if (c == 0):
			c = 255

image.save("demo_image.png", "PNG")