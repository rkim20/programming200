#I've heard of this situation before, and I'm fairly sure the better option is to switch choices. However, I didn't hear an explanation as to why this is the better option and logically, it seems like it shouldn't matter since the chances are 50 50 anyways. I hope and believe, however, that I will find out something intriguing through this assignment!

import random

def trial():
	global win

	number = random.randint(0,2) #this is the correct box or box with the car

	choice = random.randint(0,2) #this is the user's choice of box


	#Decides which box to remove
	if (number == 0) and (choice == 0):
		remove = random.randint(1,2)
	elif (number == 0) and (choice == 1):
		remove = 2
	elif (number == 0) and (choice == 2):
		remove = 1
	#------------------------------------------------
	elif (number == 1) and (choice == 0):
		remove = 2
	elif (number == 1) and (choice == 1):
		a = random.randint(0,1)
		if (a == 0):
			remove = 0
		else:
			remove = 2
	elif (number == 1) and (choice == 2):
		remove = 0
	#------------------------------------------------
	elif (number == 2) and (choice == 0):
		remove = 1
	elif (number == 2) and (choice == 1):
		remove = 0
	elif (number == 2) and (choice == 2):
		a = random.randint(0,1)
		if (a == 0):
			remove = 0
		else:
			remove = 1


	decision = "yes" #change yes/no to alter results

	if (decision == "yes") and (number == choice): #lose
		result = 1

	if (decision == "yes") and (number != choice): #win
		result = 0

	if (decision == "no") and (number == choice): #win
		result = 0

	if (decision == "no") and (number != choice): #lose
		result = 1

	if (result == 0):
		win = win + 1

#Main-----------------------------------------------------------------------
win = 0

for x in range(1000):
	trial()


print(win)








#Based on my code and the data I got from it, if the player decides to switch, they end up winning more than if they didn't switch. My number of times winning when I didn't switch were around the 300 range out of 1000 trials. However, when I decided to switch, I got within the 600 range out of 1000 for number of wins. After giving it some thought, I feel like I have some sort of reasoning that might explain why I got my results. It is written below.

#When you first choose a box, you have a 1/3 chance of getting it correct. However, after one of the boxes is revealed and doesn't contain the car, your options are now limited to 2, increasing your chance of getting the car from 1/3 to 1/2. Although the box with the car doesn't actually switch, your odds are better if you pick another time. This was the reasoning I followed.






