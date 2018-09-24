"""
Ryan Kim
Monday, September 24th, 2018
On my honor, I have neither given nor received unauthorized aid.

Description: This is an adventure game where the user must save his/her brother. They can choose the class they want. Each class has a different level of difficulty. For example, the soldier has an easy difficulty level because it has a highest amount of damage, the most amount of health, and a good chance number, thus making it easier to beat the game. After, choosing your character, you must face off against the assassin that kidnapped your brother and fight him for your brother's life.
"""



import math
import random
#-------------------------------------------------------------------------
def choosingCharacter():
	global dmg, health, chance, characterChoice

	characterChoice = input ("Type your choice: ")
	characterChoice = str(characterChoice)

	if (characterChoice == "soldier") or (characterChoice == "Soldier"):
		print ("\nYou chose the soldier!")
		print ("\n------------------------------------------------------------------------")
		dmg = 10
		health = 15
		chance = 3
	elif (characterChoice == "archer") or (characterChoice == "Archer"):
		print ("\nYou chose the archer!")
		print ("\n------------------------------------------------------------------------")
		dmg = 7
		health = 10
		chance = 4
	elif (characterChoice == "commoner") or (characterChoice == "Commoner"):
		print ("\nYou chose the commoner!")
		print ("\n------------------------------------------------------------------------")
		dmg = 5
		health = 10
		chance = 3
	else:
		print ("You didn't type your character choice.\n")
		choosingCharacter()
#-------------------------------------------------------------------------
def stats():
	global dmg, health, chance, enemydmg, enemyhealth

	print ("\nYour Stats:\n Damage:", dmg, "\n Health:", health, "\n Chance:", chance)
	print ("\nEnemy Stats:\n Damage:", enemydmg, "\n Health:", enemyhealth)
#-------------------------------------------------------------------------
def attack():
	global damageDealt, enemyhealth

	damageDealt = random.randint(0,dmg)
	enemyhealth -= damageDealt

	print ("\nYou did", damageDealt, "damage to the assassin!")
#-------------------------------------------------------------------------
def defense():
	global enemy1DamageDealt, health, enemydmg

	enemy1DamageDealt = random.randint(0,enemydmg)
	health -= enemy1DamageDealt

	print ("\nThe assassin did", enemy1DamageDealt, "damage to you!")
#-------------------------------------------------------------------------
def chanceFunction():
	global chanceGuess, chanceNumber, chance

	while True:
		try:
			chance = str(chance)
			chanceGuess = input("\nGuess a number between 0 and " + chance + ": ")
			print ("\n------------------------------------------------------------------------")
			chance = int(chance)
			chanceNumber = random.randint(0,chance)

			chanceGuess = int(chanceGuess)
			chanceNumber = int(chanceNumber)

			if (chanceGuess >= 0) and (chanceGuess <= chance):
				if (chanceGuess == chanceNumber):
					print("\nYou guessed right!")
					attack()
					break
				else:
					print("\nYou guessed wrong!")
					break
			else:
				print("\nYou didn't guess a number within the parameters. Please try again.")
				chanceFunction()
		except ValueError:
			print ("That's not a number. Try again.")
#-------------------------------------------------------------------------
def battle():
	global health, enemyhealth

	round = 1
	while (health > 0) and (enemyhealth > 0):
		print ("\n\n\n Round", round)
		attack()
		defense()
		chanceFunction()
		if (health > 0) and (enemyhealth > 0):
			stats()

		round += 1
#-------------------------------------------------------------------------
def end():
	global health, enemyhealth

	if (health > 0) and (enemyhealth <= 0):
		print ("\nYou beat the assassin! Now you can get your brother back.\n")

	elif (health <= 0) and (enemyhealth > 0):
		print ("\nYou failed to beat the assassin and save your brother. Shame on you!\n")

	elif (health <= 0) and (enemyhealth <= 0):
		print ("\nYou beat the assassin, but failed to survive.\n\nYou failed to save your brother. Shame on you!\n")
#-------------------------------------------------------------------------


dmg = 0
health = 0
chance = 0

enemydmg = 8
enemyhealth = 15



print ("You are here to save your brother! An assassin kidnapped him.\nChoose your character...\n\n")

print ("Soldier (Easy Difficulty):\n 10 dmg\n 15 health\n 3 chance\n")
print ("Archer (Medium Difficulty):\n 7 dmg\n 10 health\n 4 chance\n")
print ("Commoner (Hard Difficulty):\n 5 dmg\n 10 health\n 3 chance\n")

choosingCharacter()

print ("\nNow you must go get your brother back. In order to save him, you must beat this assassin.\n\nLook! He is coming at you right now!")

stats()

print ("\n\nWhen you attack, the damage you do is a random number between 0 and your damage stat.\n\nYour chance stat is the opportunity to attack twice. A random number between 0 and your chance stat is generated and if you guess correctly, you will get to attack twice!\n\nYou get the first strike.\n\nGood luck!")


battle()

end()