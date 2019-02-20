"""
Mini Game: 
"""

import pyglet
from pyglet.window import key
from pyglet.window import mouse


# The Window Module
# ------------------------------------------------------------------------------------------------
window = pyglet.window.Window(500, 500) #x, y
#the .window.Window function displays a window on the user’s screen with the x, and y parameters given
# def enemy():
ball_image = pyglet.image.load('gary.jpeg')
ball = pyglet.sprite.Sprite(ball_image, x=window.width-400, y=window.height)
ball.scale=.3
def update(dt):
    # Move 10 pixels per second
    ball.y -= dt * 50
# Call update 60 times a second
while ball.y>50:
    pyglet.clock.schedule_interval(update, 1/60)

# Displaying all of the events
# ------------------------------------------------------------------------------------------------
@window.event #this event helps refresh the window if there are changes within it
def on_draw():
    # window.clear()
    window.clear()
   
    # i=0
    # for i in range(0,100):
    ball.draw()
        # enemy()
        # i+=1
pyglet.app.run()#this command should always be at the end of your code because it runs your code
