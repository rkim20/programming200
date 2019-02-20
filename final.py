import pyglet
from pyglet.window import key
from pyglet.window import Window


word_list = []
correct = 0
grade = "Unknown"
answer = "nothing"
correct_catholic = True
correct_church = True
correct_priest = True
correct_swansea = True
correct_candle = True
correct_stdavids = True
correct_bishop = True
correct_canon = True
correct_baptism = True
correct_hymns = True
correct_parish = True
correct_organ = True
correct_pope = True
correct_diocese = True

window = pyglet.window.Window(500,500)

test = pyglet.text.Label('English Test!',
							font_name='Times New Roman',
							font_size=36,
							x=window.width//2, y=window.height*12/13,
							anchor_x='center', anchor_y='center')

word_instructions1 = "Your test is a word search."
word_instructions2 = "Type the word you find and press 'enter'."
word_instructions3 = "Make sure to type the word correctly to get points."
word_instructions4 = "If you are done finding words, type 'done' and then 'enter'."
word_instructions5 = "Press any key to begin."

word_instructions_text1 = pyglet.text.Label(word_instructions1,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+40,
							anchor_x='center', anchor_y='center')

word_instructions_text2 = pyglet.text.Label(word_instructions2,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2+20,
							anchor_x='center', anchor_y='center')

word_instructions_text3 = pyglet.text.Label(word_instructions3,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2,
							anchor_x='center', anchor_y='center')

word_instructions_text4 = pyglet.text.Label(word_instructions4,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//2-20,
							anchor_x='center', anchor_y='center')

word_instructions_text5 = pyglet.text.Label(word_instructions5,
							font_name='Times New Roman',
							font_size=12,
							x=window.width//2, y=window.height//4,
							anchor_x='center', anchor_y='center')

word_search = pyglet.image.load('/Users/ryankim/Desktop/programming200/wordsearch.png')
word = pyglet.sprite.Sprite(word_search, x=window.width//5.5-10, y=window.height//4)
word.scale=0.8

#-------------------------------------------------------------------------

@window.event
def on_key_press(symbol, modifiers):
	global correct, correct_catholic, correct_church, correct_priest, correct_swansea, correct_candle, correct_stdavids, correct_bishop, correct_canon, correct_baptism, correct_hymns, correct_parish, correct_organ, correct_pope, correct_diocese

	letter_pressed = str(pyglet.window.key.symbol_string(symbol))
	word_list.append(letter_pressed)
	print(letter_pressed)

	letter = pyglet.text.Label(letter_pressed,
							font_name='Times New Roman',
							font_size=36,
							x=window.width//2, y=window.height//9,
							anchor_x='center', anchor_y='center')

	score = pyglet.text.Label ('Words: ' + str(correct),
							font_name = 'Times New Roman',
							font_size = 14,
							x = (window.width//10), y = window.height*(15/16),
							anchor_x = 'center', anchor_y = 'center')

	@window.event
	def on_draw():
		window.clear()
		test.draw()
		word.draw()
		letter.draw()
		score.draw()

#-------------------------------------------------------------------------

	for x in range(len(word_list)):


		if (correct_catholic == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "C"):
					if (word_list[x+1] == "A"):
						if (word_list[x+2] == "T"):
							if (word_list[x+3] == "H"):
								if (word_list[x+4] == "O"):
									if (word_list[x+5] == "L"):
										if (word_list[x+6] == "I"):
											if (word_list[x+7] == "C"):

												print("You got 'catholic'!")
												correct += 1
												answer = "catholic"
												correct_catholic = False

												correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																			font_name = 'Times New Roman',
																			font_size = 36,
																			x = (window.width//2), y = (window.height//6),
																			anchor_x = 'center', anchor_y = 'center')

												score = pyglet.text.Label ('Words: ' + str(correct),
																			font_name = 'Times New Roman',
																			font_size = 14,
																			x = (window.width//10), y = window.height*(15/16),
																			anchor_x = 'center', anchor_y = 'center')

												@window.event
												def on_draw():
													window.clear() #Clear statement
													test.draw() #"English Test!"
													word.draw() #image
													correct_answer.draw() #Shows correct statement
													score.draw()

#--------------------------------------------------------------------------
		if (correct_church == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "C"):
					if (word_list[x+1] == "H"):
						if (word_list[x+2] == "U"):
							if (word_list[x+3] == "R"):
								if (word_list[x+4] == "C"):
									if (word_list[x+5] == "H"):
										print("You got 'church'!")
										correct += 1
										answer = "church"
										correct_church = False

										correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																	font_name = 'Times New Roman',
																	font_size = 36,
																	x = (window.width//2), y = (window.height//6),
																	anchor_x = 'center', anchor_y = 'center')

										score = pyglet.text.Label ('Words: ' + str(correct),
																	font_name = 'Times New Roman',
																	font_size = 14,
																	x = (window.width//10), y = window.height*(15/16),
																	anchor_x = 'center', anchor_y = 'center')

										@window.event
										def on_draw():
											window.clear() #Clear statement
											test.draw() #"English Test!"
											word.draw() #image
											correct_answer.draw() #Shows correct statement
											score.draw()

#--------------------------------------------------------------------------
		if (correct_priest == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "P"):
					if (word_list[x+1] == "R"):
						if (word_list[x+2] == "I"):
							if (word_list[x+3] == "E"):
								if (word_list[x+4] == "S"):
									if (word_list[x+5] == "T"):
										print("You got 'priest'!")
										correct += 1
										answer = "priest"
										correct_priest = False

										correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																	font_name = 'Times New Roman',
																	font_size = 36,
																	x = (window.width//2), y = (window.height//6),
																	anchor_x = 'center', anchor_y = 'center')

										score = pyglet.text.Label ('Words: ' + str(correct),
																	font_name = 'Times New Roman',
																	font_size = 14,
																	x = (window.width//10), y = window.height*(15/16),
																	anchor_x = 'center', anchor_y = 'center')

										@window.event
										def on_draw():
											window.clear() #Clear statement
											test.draw() #"English Test!"
											word.draw() #image
											correct_answer.draw() #Shows correct statement
											score.draw()

#--------------------------------------------------------------------------

		if (correct_swansea == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "S"):
					if (word_list[x+1] == "W"):
						if (word_list[x+2] == "A"):
							if (word_list[x+3] == "N"):
								if (word_list[x+4] == "S"):
									if (word_list[x+5] == "E"):
										if (word_list[x+6] == "A"):
											print("You got 'swansea'!")
											correct += 1
											answer = "swansea"
											correct_swansea = False

											correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																		font_name = 'Times New Roman',
																		font_size = 36,
																		x = (window.width//2), y = (window.height//6),
																		anchor_x = 'center', anchor_y = 'center')

											score = pyglet.text.Label ('Words: ' + str(correct),
																		font_name = 'Times New Roman',
																		font_size = 14,
																		x = (window.width//10), y = window.height*(15/16),
																		anchor_x = 'center', anchor_y = 'center')

											@window.event
											def on_draw():
												window.clear() #Clear statement
												test.draw() #"English Test!"
												word.draw() #image
												correct_answer.draw() #Shows correct statement
												score.draw()

#--------------------------------------------------------------------------

		if (correct_candle == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "C"):
					if (word_list[x+1] == "A"):
						if (word_list[x+2] == "N"):
							if (word_list[x+3] == "D"):
								if (word_list[x+4] == "L"):
									if (word_list[x+5] == "E"):
										print("You got 'candle'!")
										correct += 1
										answer = "candle"
										correct_candle = False

										correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																	font_name = 'Times New Roman',
																	font_size = 36,
																	x = (window.width//2), y = (window.height//6),
																	anchor_x = 'center', anchor_y = 'center')

										score = pyglet.text.Label ('Words: ' + str(correct),
																	font_name = 'Times New Roman',
																	font_size = 14,
																	x = (window.width//10), y = window.height*(15/16),
																	anchor_x = 'center', anchor_y = 'center')

										@window.event
										def on_draw():
											window.clear() #Clear statement
											test.draw() #"English Test!"
											word.draw() #image
											correct_answer.draw() #Shows correct statement
											score.draw()

#--------------------------------------------------------------------------

		if (correct_stdavids == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "S"):
					if (word_list[x+1] == "T"):
						if (word_list[x+2] == "D"):
							if (word_list[x+3] == "A"):
								if (word_list[x+4] == "V"):
									if (word_list[x+5] == "I"):
										if (word_list[x+6] == "D"):
											if (word_list[x+7] == "S"):
												print("You got 'St Davids'!")
												correct += 1
												answer = "st davids"
												correct_stdavids = False

												correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																			font_name = 'Times New Roman',
																			font_size = 36,
																			x = (window.width//2), y = (window.height//6),
																			anchor_x = 'center', anchor_y = 'center')

												score = pyglet.text.Label ('Words: ' + str(correct),
																			font_name = 'Times New Roman',
																			font_size = 14,
																			x = (window.width//10), y = window.height*(15/16),
																			anchor_x = 'center', anchor_y = 'center')

												@window.event
												def on_draw():
													window.clear() #Clear statement
													test.draw() #"English Test!"
													word.draw() #image
													correct_answer.draw() #Shows correct statement
													score.draw()

#--------------------------------------------------------------------------

		if (correct_bishop == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "B"):
					if (word_list[x+1] == "I"):
						if (word_list[x+2] == "S"):
							if (word_list[x+3] == "H"):
								if (word_list[x+4] == "O"):
									if (word_list[x+5] == "P"):
										print("You got 'bishop'!")
										correct += 1
										answer = "bishop"
										correct_bishop = False

										correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																	font_name = 'Times New Roman',
																	font_size = 36,
																	x = (window.width//2), y = (window.height//6),
																	anchor_x = 'center', anchor_y = 'center')

										score = pyglet.text.Label ('Words: ' + str(correct),
																	font_name = 'Times New Roman',
																	font_size = 14,
																	x = (window.width//10), y = window.height*(15/16),
																	anchor_x = 'center', anchor_y = 'center')

										@window.event
										def on_draw():
											window.clear() #Clear statement
											test.draw() #"English Test!"
											word.draw() #image
											correct_answer.draw() #Shows correct statement
											score.draw()

#--------------------------------------------------------------------------

		if (correct_canon == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "C"):
					if (word_list[x+1] == "A"):
						if (word_list[x+2] == "N"):
							if (word_list[x+3] == "O"):
								if (word_list[x+4] == "N"):
									print("You got 'canon'!")
									correct += 1
									answer = "canon"
									correct_canon = False

									correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																font_name = 'Times New Roman',
																font_size = 36,
																x = (window.width//2), y = (window.height//6),
																anchor_x = 'center', anchor_y = 'center')

									score = pyglet.text.Label ('Words: ' + str(correct),
																font_name = 'Times New Roman',
																font_size = 14,
																x = (window.width//10), y = window.height*(15/16),
																anchor_x = 'center', anchor_y = 'center')

									@window.event
									def on_draw():
										window.clear() #Clear statement
										test.draw() #"English Test!"
										word.draw() #image
										correct_answer.draw() #Shows correct statement
										score.draw()

#--------------------------------------------------------------------------

		if (correct_baptism == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "B"):
					if (word_list[x+1] == "A"):
						if (word_list[x+2] == "P"):
							if (word_list[x+3] == "T"):
								if (word_list[x+4] == "I"):
									if (word_list[x+5] == "S"):
										if (word_list[x+6] == "M"):
											print("You got 'baptism'!")
											correct += 1
											answer = "baptism"
											correct_baptism = False

											correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																		font_name = 'Times New Roman',
																		font_size = 36,
																		x = (window.width//2), y = (window.height//6),
																		anchor_x = 'center', anchor_y = 'center')

											score = pyglet.text.Label ('Words: ' + str(correct),
																		font_name = 'Times New Roman',
																		font_size = 14,
																		x = (window.width//10), y = window.height*(15/16),
																		anchor_x = 'center', anchor_y = 'center')

											@window.event
											def on_draw():
												window.clear() #Clear statement
												test.draw() #"English Test!"
												word.draw() #image
												correct_answer.draw() #Shows correct statement
												score.draw()

#--------------------------------------------------------------------------

		if (correct_organ == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "O"):
					if (word_list[x+1] == "R"):
						if (word_list[x+2] == "G"):
							if (word_list[x+3] == "A"):
								if (word_list[x+4] == "N"):
									print("You got 'organ'!")
									correct += 1
									answer = "organ"
									correct_organ = False

									correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																font_name = 'Times New Roman',
																font_size = 36,
																x = (window.width//2), y = (window.height//6),
																anchor_x = 'center', anchor_y = 'center')

									score = pyglet.text.Label ('Words: ' + str(correct),
																font_name = 'Times New Roman',
																font_size = 14,
																x = (window.width//10), y = window.height*(15/16),
																anchor_x = 'center', anchor_y = 'center')

									@window.event
									def on_draw():
										window.clear() #Clear statement
										test.draw() #"English Test!"
										word.draw() #image
										correct_answer.draw() #Shows correct statement
										score.draw()

#--------------------------------------------------------------------------

		if (correct_hymns == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "H"):
					if (word_list[x+1] == "Y"):
						if (word_list[x+2] == "M"):
							if (word_list[x+3] == "N"):
								if (word_list[x+4] == "S"):
									print("You got 'hymns'!")
									correct += 1
									answer = "hymns"
									correct_hymns = False

									correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																font_name = 'Times New Roman',
																font_size = 36,
																x = (window.width//2), y = (window.height//6),
																anchor_x = 'center', anchor_y = 'center')

									score = pyglet.text.Label ('Words: ' + str(correct),
																font_name = 'Times New Roman',
																font_size = 14,
																x = (window.width//10), y = window.height*(15/16),
																anchor_x = 'center', anchor_y = 'center')

									@window.event
									def on_draw():
										window.clear() #Clear statement
										test.draw() #"English Test!"
										word.draw() #image
										correct_answer.draw() #Shows correct statement
										score.draw()

#--------------------------------------------------------------------------

		if (correct_parish == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "P"):
					if (word_list[x+1] == "A"):
						if (word_list[x+2] == "R"):
							if (word_list[x+3] == "I"):
								if (word_list[x+4] == "S"):
									if (word_list[x+5] == "H"):
										print("You got 'parish'!")
										correct += 1
										answer = "parish"
										correct_parish = False

										correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																	font_name = 'Times New Roman',
																	font_size = 36,
																	x = (window.width//2), y = (window.height//6),
																	anchor_x = 'center', anchor_y = 'center')

										score = pyglet.text.Label ('Words: ' + str(correct),
																	font_name = 'Times New Roman',
																	font_size = 14,
																	x = (window.width//10), y = window.height*(15/16),
																	anchor_x = 'center', anchor_y = 'center')

										@window.event
										def on_draw():
											window.clear() #Clear statement
											test.draw() #"English Test!"
											word.draw() #image
											correct_answer.draw() #Shows correct statement
											score.draw()

#--------------------------------------------------------------------------

		if (correct_pope == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "P"):
					if (word_list[x+1] == "O"):
						if (word_list[x+2] == "P"):
							if (word_list[x+3] == "E"):
								print("You got 'pope'!")
								correct += 1
								answer = "pope"
								correct_pope = False

								correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
															font_name = 'Times New Roman',
															font_size = 36,
															x = (window.width//2), y = (window.height//6),
															anchor_x = 'center', anchor_y = 'center')

								score = pyglet.text.Label ('Words: ' + str(correct),
															font_name = 'Times New Roman',
															font_size = 14,
															x = (window.width//10), y = window.height*(15/16),
															anchor_x = 'center', anchor_y = 'center')

								@window.event
								def on_draw():
									window.clear() #Clear statement
									test.draw() #"English Test!"
									word.draw() #image
									correct_answer.draw() #Shows correct statement
									score.draw()

#--------------------------------------------------------------------------

		if (correct_diocese == True):
			if (letter_pressed == "ENTER"):
				if (word_list[x] == "D"):
					if (word_list[x+1] == "I"):
						if (word_list[x+2] == "O"):
							if (word_list[x+3] == "C"):
								if (word_list[x+4] == "E"):
									if (word_list[x+5] == "S"):
										if (word_list[x+6] == "E"):
											print("You got 'diocese'!")
											correct += 1
											answer = "diocese"
											correct_diocese = False

											correct_answer = pyglet.text.Label ("You got '" + answer + "'!",
																		font_name = 'Times New Roman',
																		font_size = 36,
																		x = (window.width//2), y = (window.height//6),
																		anchor_x = 'center', anchor_y = 'center')

											score = pyglet.text.Label ('Words: ' + str(correct),
																		font_name = 'Times New Roman',
																		font_size = 14,
																		x = (window.width//10), y = window.height*(15/16),
																		anchor_x = 'center', anchor_y = 'center')

											@window.event
											def on_draw():
												window.clear() #Clear statement
												test.draw() #"English Test!"
												word.draw() #image
												correct_answer.draw() #Shows correct statement
												score.draw()

#--------------------------------------------------------------------------

		if (letter_pressed == "ENTER"):
			if (word_list[x] == "D"):
				if (word_list[x+1] == "O"):
					if (word_list[x+2] == "N"):
						if (word_list[x+3] == "E"):

							if (correct == 12):
								grade = "A+"
							elif (correct >= 10):
								grade = "A"
							elif (correct >= 8):
								grade = "A-"
							elif (correct >= 6):
								grade = "B+"
							elif (correct >= 4):
								grade = "B-"
							elif (correct >= 2):
								grade = "C+"
							else:
								grade = "F"

							grade_received = pyglet.text.Label ('Your grade: ' + grade,
														font_name = 'Times New Roman',
														font_size = 36,
														x = (window.width//2), y = (window.height//2),
														anchor_x = 'center', anchor_y = 'center')

							@window.event
							def on_draw():
								window.clear() #Clear statement
								test.draw() #"English Test!"
								grade_received.draw()


	if (correct == 14):
		@window.event
		def on_draw():
			window.clear()
			test.draw()
			grade_received.draw()

#-----------------------------------------------------------------------
#Display

score = pyglet.text.Label ('Words: ' + str(correct),
							font_name = 'Times New Roman',
							font_size = 14,
							x = (window.width//10), y = window.height*(15/16),
							anchor_x = 'center', anchor_y = 'center')

@window.event
def on_draw():
	window.clear()
	test.draw()
	word_instructions_text1.draw()
	word_instructions_text2.draw()
	word_instructions_text3.draw()
	word_instructions_text4.draw()
	word_instructions_text5.draw()


pyglet.app.run()










