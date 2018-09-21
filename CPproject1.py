import math
import random

#-------------------------------------------------------------------------
def choosingCharacter():
	characterChoice = input ("Type your choice ")
	characterChoice = str(characterChoice)

	if (characterChoice == "soldier") or (characterChoice == "Soldier"):
		print ("\nYou chose the soldier!")
		dmg = 4
		health = 15
		chance = 3
	elif (characterChoice == "archer") or (characterChoice == "Archer"):
		print ("\nYou chose the archer!")
		dmg = 8
		health = 10
		chance = 5
	else:
		print ("You didn't type your character choice./n")
#-------------------------------------------------------------------------
def switchString():
	dmg = str(dmg)
	health = str(health)
	chance = str(chance)

	enemydmg = str(enemydmg)
	enemyhealth = str(enemyhealth)
#-------------------------------------------------------------------------
def switchInt():
	dmg = int(dmg)
	health = int(health)
	chance = int(chance)

	enemydmg = int(enemydmg)
	enemyhealth = int(enemyhealth)
#-------------------------------------------------------------------------
def attack():
	damageDealt = random.randint(0,dmg)
	enemy1health -= damageDealt
#-------------------------------------------------------------------------
def defense():
	enemy1DamageDealt = random.randint(0,enemy1dmg)
	health -= enemy1DamageDealt
#-------------------------------------------------------------------------
def chance():
	chanceGuess = input("Guess a number between 0 and", chance)
	chanceNumber = random.randint(0,chance)
	if (chanceGuess == chanceNumber):
		print("\nYou guessed right!")
		fighting()
	else:
		print("\nYou guessed wrong!")
#-------------------------------------------------------------------------


dmg = 0
health = 0
chance = 0

enemydmg = 10
enemyhealth = 20



print ("You are here to save your brother! An assassin kidnapped him.\nChoose your character...\n\n")

print ("Soldier:\n 5 dmg\n 10 health\n 3 chance\n")
print ("Archer:\n 9 dmg\n 10 health\n 5 chance\n")

choosingCharacter()

print ("\nNow you must go get your brother back. In order to save him, you must beat this assassin.\n\nLook! He is coming at you right now!")

switchString()

print ("\n\nYour Stats:\n Damage: " + dmg + "\n Health: " + health + "\n Chance: " + chance)
print ("\n\nEnemy Stats:\n Damage: " + enemydmg + "\n Health: " + enemyhealth)

switchInt()

print ("\n\n When you attack, the damage you do is a random number between 0 and your damage stat.\nYour chance stat is the opportunity to attack twice. A random number between 0 and your chance stat is generated and if you guess correctly, you will get to attack twice!\nYou get the first attack. Good luck!")


#-------------------------------------------------------------------------
#Fighting

attack()

defense()

chance()



# - finish fight (if statement for alive/boolean for alive)