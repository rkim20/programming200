import pyglet
from pyglet.window import key

word_list = []

window = pyglet.window.Window(500,500)
label = pyglet.text.Label('Test!',
							font_name='Times New Roman',
							font_size=36,
							x=window.width//2, y=(window.height//3)*2,
							anchor_x='center', anchor_y='center')

word_search = pyglet.image.load('wordsearch.png')
word = pyglet.sprite.Sprite(word_search, x=window.width//2, y=window.height//2)

@window.event
def on_key_press(symbol, modifiers):
	if (symbol == key.A):
		word_list.append('a')
	if (symbol == key.B):
		word_list.append('b')
	if (symbol == key.C):
		word_list.append('c')
	if (symbol == key.ENTER):
		print("You entered " + word_list)


#-----------------------------------------------------------------------
#Display

@window.event
def on_draw():
	window.clear()
	label.draw()
	word.draw()


pyglet.app.run()