
"""
while True:
	try:
		num = int(input("Pick a number between 1 and 5: "))
		while num < 1 or num > 5:
			num = int(input("That's not in the right range. Please choose a number between 1 and 5: "))
		break

	except ValueError or NameError:
		print("That's not a number. Try again.")
"""
import random
import math

chance = 5

while True:
	try: 
		chance = str(chance)
		chanceGuess = input("\nGuess a number between 0 and " + chance + ": ")
		chance = int(chance)
		chanceNumber = random.randint(0,chance)

		chanceGuess = int(chanceGuess)
		chanceNumber = int(chanceNumber)

		if (chanceGuess >= 0) and (chanceGuess <= chance):
			if (chanceGuess == chanceNumber):
				print("\nYou guessed right!")
				#attack()
				break
			else:
				print("\nYou guessed wrong!")
				break
		else:
			print("\nYou didn't guess a number within the parameters. Please try again.")
	except ValueError:
		print ("That's not a number. Try again.")



"""
while num > count:
	print ("Hi")
	count+=1
"""

