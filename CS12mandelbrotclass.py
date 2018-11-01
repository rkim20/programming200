#Ryan Kim
#Date Due: Thursday, November 1st (Extended due date)
#On my honor, I have neither given nor received unauthorized aid.

#Explanation
#In this project, I drew two images using the Mandelbrot set and one using the Julia set. When going about this project, I started with the basics: finding the right zoom parameters and playing around with the colors. After that, I went on to find an extra element that I could add to the image. This could be playing with colorsys or adding a filter or any other type of creative function I could find. With the Julia set, I took some time before starting this process to really understand the differences from the Mandelbrot set. I then made sure I got the basic code for the Julia set down before going into the zoom and coloring. Overall, I think the challenge in this project lay in the creativity of it. As we went over the code for the Mandelbrot set and had resources on the Julia set, figuring out how to draw the images wasn't the hardest part of the code. Rather, it was finding the perfect creative element to add to the image. In my experience, there were many different ways to make the image look fantastic, but this didn't always require a lot of work. On the other hand, there were various functions or elements I could have added to my image that would have required significant effort, but they didn't make the image look nice. It was hard for me to find the perfect element of creativity to add to my image that would enhance it both aesthetically as well as in terms of coding.


"""
Sources

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
#For this image, I wanted to stray away from the typical images that were posted on the wall of the class. I looked carefully at the original Mandelbrot set image and found the horizontal line on the left side of the image to be very interesting. I picked the zoom parameters according to that and found an image that I found very interesting. For some reason, the image I saw kept reminding me of a compass, and I kept getting a sailing or ocean vibe from the image. I think this is due to the way the lines are drawn as well as the wavy lines that move horizontally all across the image. After finding this, I used the colorsys function to apply HSV color values which allowed me to focus on a specific range of the color wheel while adjuting the brightness and saturation of that color. Regarding the HSV colormode, I programmed it so that I could input HSV values within specific ranges that I chose. Those values would be proportionized into values that would fit into the colorsys function and would provide the RGB values for the color I wanted. Finally, these RGB values would be in a different scale, so I had to multiply them into the proper RGB values that were accepted when adding each pixel. After doing all this, I was playing around with different color schemes that I found extremely pleasing. While doing this, I came upon a method for inverting the colors. I tried inverting the colors with each of the color schemes that I had found and automatically chose the current color scheme. Not only do the shades of blue match perfectly with each other, but they also add to the effect of the ocean and sailing which I greatly appreciated.

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
		h = ((i*2)%50)-10 #range is 255 - This mathematical arrangement allows me to choose the particular color range and how big the range is (red here, but blue because it was inverted)
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
#Second Image - Julia Set
#For this image, I drew the Julia set. After watching several of the videos attached about the two sets, I understood the difference and was able to easily change the code. Specifically, instead of having c be every single pixel, I played around with the specific c values to find a cool pattern. Additionally, I made z a complex number of every single pixel similar to the c values of the Mandelbrot set. This provided me with the Julia set. After I successfully created the Julia set, I played around with the zoom parameters. I found a specific pattern of spiralling spirals that I found extremely interesting. It was an infinite spiral made of never ending spirals. After finding this pattern, I went on to finding the right color scheme that would match this mesmerizing image. After playing around for a while, I decided to try applying the HSV color scheme to the image just to see how things would look. I found that the image had a whole different quality to it. It changed from mesmerizing and a bit dull to full of life and color. I played around with the different values a bit more to create a painting type image. The way the saturation and value are adjusted make the colors look like they were painted. In addition to that, they have a drooping effect at some points that look like a drip of paint overlapped into a different color. I fell in love with the way this image looked like a painting and decided it was perfect.

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
#For the final image of the Mandelbrot set, I attempted to find the right zoom parameters that would look like a snowflake or have that quality to it. I decided not to use the HSV color scheme in this image. When playing around with the colors, I decided to invert the colors again. In this case, I found that there was a milky off-white background to the image that I really enjoyed. I played off of this to add a black color which juxtaposed the white background. In addition, having the green shade to the black edges gave a glowing effect to the image. Finally, I added a filter to the image that smoothed it out. There were a lot of small details in the image that looked very pixelated, and I added this filter in order to blur these parts out and make the image look cleaner as a whole.

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




