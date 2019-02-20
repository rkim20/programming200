import pyglet
from pyglet.window import key
from pyglet.window import Window

window = pyglet.window.Window(800,600)

score = 0

instructions1 = ("You will live as a Choate student and go through a typical day at Choate.")
instructions2 = ("You will make decisions and undergo the rigors and choices that students make.")
instructions3 = ("At the end of the day, you will receive a grade based on your performance.")
instructions4 = ("Good luck.")
instructions5 = ("Press '1' to start")

game_title = pyglet.text.Label('Day in the Life: Choate Student',
							font_name='Times New Roman',
							font_size=28,
							x=window.width//2, y=window.height*6/8,
							anchor_x='center', anchor_y='center')

instructions_text1 = pyglet.text.Label(instructions1,
							font_name='Times New Roman',
							font_size=11,
							x=window.width//2, y=window.height//2+20,
							anchor_x='center', anchor_y='center')

instructions_text2 = pyglet.text.Label(instructions2,
							font_name='Times New Roman',
							font_size=11,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

instructions_text3 = pyglet.text.Label(instructions3,
							font_name='Times New Roman',
							font_size=11,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

instructions_text4 = pyglet.text.Label(instructions4,
							font_name='Times New Roman',
							font_size=11,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

instructions_text5 = pyglet.text.Label(instructions5,
							font_name='Times New Roman',
							font_size=11,
							x=window.width//2, y=window.height//2-90,
							anchor_x='center', anchor_y='center')

wake_title = ("Wake Up")

wake_description = ("7:30AM")

wake1 = ("In the faint distance of your mind, you hear your alarm start to go off. You instinctively grab your phone and press the snooze button.")

wake2 = ("You know you should get up now, but your mind and body push you to close your eyes.")

wake3 = ("Your roommate has a sleep-in, and you know he will not wake you up if you go back to sleep.")

wake4 = ("You are faced with a choice.")

wake5 = ("Let your body rest and skip your first period class")

wake6 = ("or")

wake7 = ("Suffer through the morning challenges and get ready for school")

wake8 = ("Press 'w' to wake up or 's' to continue sleeping")

wake_title_text = pyglet.text.Label(wake_title,
							font_name='Times New Roman',
							font_size=20,
							x=window.width//2, y=window.height*10/11,
							anchor_x='center', anchor_y='center')

wake_description_text = pyglet.text.Label(wake_description,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height*10/11 - 30,
							anchor_x='center', anchor_y='center')

wake_text1 = pyglet.text.Label(wake1,
							font_name='Times New Roman',
							font_size=10,
							x=window.width//2, y=window.height//2-60,
							anchor_x='center', anchor_y='center')

wake_text2 = pyglet.text.Label(wake2,
							font_name='Times New Roman',
							font_size=10,
							x=window.width//2, y=window.height//2-80,
							anchor_x='center', anchor_y='center')

wake_text3 = pyglet.text.Label(wake3,
							font_name='Times New Roman',
							font_size=10,
							x=window.width//2, y=window.height//2-100,
							anchor_x='center', anchor_y='center')

wake_text4 = pyglet.text.Label(wake4,
							font_name='Times New Roman',
							font_size=10,
							x=window.width//2, y=window.height//2-120,
							anchor_x='center', anchor_y='center')

wake_text5 = pyglet.text.Label(wake5,
							font_name='Times New Roman',
							font_size=10,
							x=window.width//2, y=window.height//2-160,
							anchor_x='center', anchor_y='center')

wake_text6 = pyglet.text.Label(wake6,
							font_name='Times New Roman',
							font_size=10,
							x=window.width//2, y=window.height//2-190,
							anchor_x='center', anchor_y='center')

wake_text7 = pyglet.text.Label(wake7,
							font_name='Times New Roman',
							font_size=10,
							x=window.width//2, y=window.height//2-220,
							anchor_x='center', anchor_y='center')

wake_text8 = pyglet.text.Label(wake8,
							font_name='Times New Roman',
							font_size=10,
							x=window.width//2, y=window.height//2-270,
							anchor_x='center', anchor_y='center')



sleep_decision1 = ("You slept through your first class.")

sleep_decision2 = ("Your roommate woke you up when his alarm went off, and you feel much better now.")

sleep_decision3 = ("You are more prepared for your next class and will be more efficient while working.")

wake_decision1 = ("You decided to push yourself and got up.")

wake_decision2 = ("You were groggy but got through your first class where you learned a lot for an upcoming test.")

sleep_decision_text1 = pyglet.text.Label(sleep_decision1,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height//2+40,
							anchor_x='center', anchor_y='center')

sleep_decision_text2 = pyglet.text.Label(sleep_decision2,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

sleep_decision_text3 = pyglet.text.Label(sleep_decision3,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height//2-40,
							anchor_x='center', anchor_y='center')

wake_decision_text1 = pyglet.text.Label(wake_decision1,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height//2+20,
							anchor_x='center', anchor_y='center')

wake_decision_text2 = pyglet.text.Label(wake_decision2,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

continue2 = ("Press '2' to continue")

continue_text2 = pyglet.text.Label(continue2,
							font_name='Times New Roman',
							font_size=15,
							x=window.width//2, y=window.height//2-120,
							anchor_x='center', anchor_y='center')

#-------------------------------------------------------------------

@window.event
def on_key_press(symbol, modifiers):
	global score

	if (symbol == key._1): #GAME STARTS
		@window.event
		def on_draw():
			window.clear()
			wake_title_text.draw()
			wake_text1.draw()
			wake_text2.draw()
			wake_text3.draw()
			wake_text4.draw()
			wake_text5.draw()
			wake_text6.draw()
			wake_text7.draw()
			wake_text8.draw()
			wake_description_text.draw()

	if (symbol == key.S):
		score += 0
		@window.event
		def on_draw():
			window.clear()
			sleep_decision_text1.draw()
			sleep_decision_text2.draw()
			sleep_decision_text3.draw()
			continue_text2.draw()

	if (symbol == key.W):
		score += 1
		@window.event
		def on_draw():
			window.clear()
			wake_decision_text1.draw()
			wake_decision_text2.draw()
			continue_text2.draw()

	if (symbol == key._2):
		@window.event
		def on_draw():
			window.clear
			#Timeline - conference, classes, lunch
			#Decision - Free




#-------------------------------------------------------------------

@window.event
def on_draw():
	window.clear()
	game_title.draw()
	instructions_text1.draw()
	instructions_text2.draw()
	instructions_text3.draw()
	instructions_text4.draw()
	instructions_text5.draw()


pyglet.app.run()










"""
To Do
- Extension
- Finish Decisions/Story
- Input Games
- Take/Add Pictures
- Calculate and Score Grade
"""








