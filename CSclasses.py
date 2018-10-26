class Dog:

	#Constructor
	def __init__(self, name, fullness, energy): #initiate - just syntax needed

		#scale out of 10
		self.fullness = fullness
		self.energy = energy
		self.happiness = 5
		self.name = name

	#Methods - don't include user input or printing in methods
	def play(self):
		if (self.energy > 0) and (self.fullness > 0):
			self.happiness += 1
			self.energy -= 1
			self.fullness -= 1
			status = self.name + " played and it was fun!"
		else:
			status = "Erm, " + self.name + " needs to not play right now. Maybe try a nap or some food?"
		return status

	def stats(self):
		info = "Name: " + self.name
		info += "\nEnergy: " + str(self.energy)
		info += "\nHappiness: " + str(self.happiness)
		info += "\nFullness: " + str(self.fullness)
		return info




dog1 = Dog("Tetris", 8, 2)
dog2 = Dog("Bat", 5, 2)

print(dog1.stats())
print(dog2.stats())

dog1.play()
dog2.play()
dog1.play()

print(dog2.play())
print(dog2.play())
print(dog2.play())
print(dog2.play())
print(dog2.play())
print(dog2.play())
print(dog2.play())
print(dog2.play())
print(dog2.play())
print(dog2.play())



print(dog1.stats())
print(dog2.stats())







