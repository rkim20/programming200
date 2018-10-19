from PIL import Image

imgx = 400
imgy = 400

image = Image.new("RGB", (imgx,imgy))


#----------------------------------------------
#For rows that have the first block as a red block
c = 0
b = 40

e = 0
f = 40

for j in range(5):
	while(b < 440):
		for x in range(c,b):
			for y in range(e,f):
				image.putpixel((x,y),(255,0,0))
		c += 80
		b += 80
	c = 0
	b = 40
	e += 80
	f += 80
#----------------------------------------------
#For rows that have the first block as a black block
k = 40
j = 80

l = 40
m = 80

for i in range (5):
	while(j < 440):
		for x in range(k,j):
			for y in range(l,m):
				image.putpixel((x,y),(255,0,0))
		k += 80
		j += 80
	k = 40
	j = 80
	l += 80
	m += 80
#----------------------------------------------


image.save("checkerboard.png","PNG")