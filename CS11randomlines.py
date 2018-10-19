import random

from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB",(imgx,imgy))



startingLocation = random.randint(10,imgx-10)

image.putpixel((startingLocation,0),(255,0,0))

x = startingLocation + random.randint(-1,2)
y = 1

while (y < 511):

	if (x < 10):
		x += random.randint(0,2)
	elif (x > 502):
		x -= random.randint(0,2)
	else:
		if (x > startingLocation + 10):
			x -= random.randint(0,2)
		elif(x < startingLocation - 10):
			x += random.randint(0,2)

		x += random.randint(-1,2)
	
	y += 1

	image.putpixel((x,y), (255,0,0))




image.save("randomlines.png", "PNG")