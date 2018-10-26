class Dog:
	#Constructor
	def __init__(self, name, energy, happiness, anger):
		self.name = name
		self.energy = energy
		self.happiness = happiness
		self.anger = anger

	#Methods
	def play():
		if (self.energy > 0):
			self.happiness += 1
			self.anger -= 1
			self.energy -= 1
			status = self.name + " played and had a good time!"
		else:
			status = self.name " doesn't have enough energy to play!"
		return status

	def eat():
		if (self.energy < 10):
			self.happiness += 1
			self.anger -= 1
			self.energy += 3
			eatStatus = self.name + " ate well!"
		else:
			eatStatus = "Watch out! " + self.name + " is getting fat!"
		return status

	def sleep():
		if (self.energy < 10):
			self.happiness += 1
			self.anger -= 2
			self.energy += 5
			sleepStatus = self.name + " slept super well!"
		else:
			sleepStatus = self.name + " has too much energy to sleep!"

	def bite():

	def stats():