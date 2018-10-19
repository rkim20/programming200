#Ryan Kim
#Due: Tuesday, October 19th
#I had trouble starting, so I started by writing everything out and not finding a more efficient way to write the code. You can see this in the way I listed the c values. I wanted to get everything working before I went back to edit and revise the code. I also wanted to get the code working with the 3x3 first, but I struggled a lot. Specifically, I had a hard time working on the c[] list and making the grid. I tried hard to find a better way to do it, but I eventually moved on after spending too much time on that detail. I also had an index error which I couldn't understand. I spent quite a while on this as I kept on thinking that changing one thing would get it to work, but I ended up not being able to get my code to work.



import random

from PIL import Image


imgx = 3
imgy = 3
image = Image.new("RGB",(imgx,imgy))

c = []

c[0] = [-2,2]
c[1] = [0,2]
c[2] = [2,2]

c[3] = [-2,0]
c[4] = [0,0]
c[5] = [2,0]

c[6] = [-2,-2]
c[7] = [0,-2]
c[8] = [2,-2]


for x in range (10):
	#a,b is the "c" value
	a,b = c[x]
	znew = a,b

	if (a**2 + b**2 >= 2):
		image.putpixel(c[x],(255,0,0))

	else:
		znew = a,b + znew
		d,e = znew
		if (d**2 + e**2 >= 2):
			image.putpixel(c[x],(0,255,0))

		else:
			image.putpixel(c[x],(0,0,255))





image.putpixel((0,0),(255,0,0))


image.save("mandelbrot.png", "PNG")