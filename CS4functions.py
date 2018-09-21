"""
def greetings(someone):
	someone = str(someone)
	print("Hello " + someone + "!")


greetings("Ryan")
greetings("George")
greetings(5)
"""

#--------------------------------------------------------------------

"""
def start():
	result = input("You are here to save the princess! \n\n She has been kidnapped by Bowser. You are at a fork in the road, and you can either \n\n 1) Go ahead and save the Princess or \n 2) Turn back in shame\n\n")
	if (result == "1"):
		savePrincess()
	elif (result == "2"):
		shame()
	else:
		print("I don't know what",result,"means. Please type a 1 or a 2.")
		start()


def savePrincess():
	print("You have saved the Princess!")

def shame():
	print("The Princess died at the hands of Bowser. Shame on you!")

start()
"""

#---------------------------------------------------------------------

import random
import math

number = random.randint(0,20)

def guessNumber():
	guess = input("Input an integer between 0 and 20\n")
	guess = float(guess)
	guess = math.floor(guess)

	if (guess >= 0) and (guess <= 20):
		if (guess == number):
			print("Correct!")
		elif (guess < number):
			print("Oops! Your number was too low!")
			guessNumber()
		elif (guess > number):
			print("Oops! Your number was too high!")
			guessNumber()
	else:
		print("You didn't select a number between 0 and 20. Please try again.")
		guessNumber()


guessNumber()



