class Card:

	#Constructor
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank



	def __str__(self):
		if (self.rank == 11):
			return("Jack of " + self.suit)
		elif (self.rank == 12):
			return("Queen of " + self.suit)
		elif (self.rank == 13):
			return("King of " + self.suit)
		elif (self.rank == 14):
			return("Ace of " + self.suit)
		else:
			return(self.rank + " of " + self.suit)