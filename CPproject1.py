import math
import random

#-------------------------------------------------------------------------
def choosingCharacter():
	global dmg, health, chance, characterChoice

	characterChoice = input ("Type your choice ")
	characterChoice = str(characterChoice)

	if (characterChoice == "soldier") or (characterChoice == "Soldier"):
		print ("\nYou chose the soldier!")
		dmg = 6
		health = 15
		chance = 3
	elif (characterChoice == "archer") or (characterChoice == "Archer"):
		print ("\nYou chose the archer!")
		dmg = 9
		health = 10
		chance = 5
	else:
		print ("You didn't type your character choice.\n")
#-------------------------------------------------------------------------
def switchString():
	global dmg, health, chance, enemydmg, enemyhealth

	dmg = str(dmg)
	health = str(health)
	chance = str(chance)

	enemydmg = str(enemydmg)
	enemyhealth = str(enemyhealth)
#-------------------------------------------------------------------------
def switchInt():
	global dmg, health, chance, enemydmg, enemyhealth

	dmg = int(dmg)
	health = int(health)
	chance = int(chance)

	enemydmg = int(enemydmg)
	enemyhealth = int(enemyhealth)
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

	chance = str(chance)
	chanceGuess = input("\nGuess a number between 0 and " + chance)
	chance = int(chance)
	chanceNumber = random.randint(0,chance)

	chanceGuess = int(chanceGuess)
	chanceNumber = int(chanceNumber)

	if (chanceGuess >= 0) and (chanceGuess <= chance):
		if (chanceGuess == chanceNumber):
			print("\nYou guessed right!")
			attack()
		else:
			print("\nYou guessed wrong!")
	else:
		print("\nYou didn't guess a number within the parameters. Please try again.")
		chanceFunction()
#-------------------------------------------------------------------------
def battle():
	global health, enemyhealth

	round = 1
	while (health > 0) and (enemyhealth > 0):
		print ("\n\n\n Round", round)
		attack()
		defense()
		chanceFunction()
		stats()

		round += 1
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

#switchString()

stats()

#switchInt()

print ("\n\nWhen you attack, the damage you do is a random number between 0 and your damage stat.\n\nYour chance stat is the opportunity to attack twice. A random number between 0 and your chance stat is generated and if you guess correctly, you will get to attack twice!\n\nYou get the first strike.\n\nGood luck!")


battle()

if (health > 0) and (enemyhealth <= 0):
	print ("\nYou beat the assassin! Now you can get your brother back.")

elif (health <= 0) and (enemyhealth > 0):
	print ("\nYou failed to beat the assassin and save your brother. Shame on you!")



	#if character choice isn't "archer" or "soldier" then redo - command