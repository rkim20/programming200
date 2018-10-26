import random

class account():

	#Constructor
	def __init___(self):
		self.balance = initialBalance
		self.pinNumber = pinNumber
		self.accountNumber
		self.working


	#Methods
	def openAccount(self):
		self.accountNumber = random.randint(10000,99999)

		status = "Balance: $" + initialBalance + "\nPin Number: " + pinNumber + "\nAccount Number: " + str(self.accountNumber)

		return status



	def withdraw(self):
		balance = initialBalance

		balance -= withdraw

		status = "You withdrew $" + withdraw + ". Your account balance is now $" + balance

		return status




#----------------------------------------------------------------------------------------------

account1 = account()
balance = 0


initialBalance = input("How much money would you like to deposit into this account? ")
pinNumber = input("\n\nWhat would you like your pin number to be? ")

print (account1.openAccount())

#User Actions
option = input("What would you like to do today?\n\n 1.) Withdraw\n\n 2.) Deposit\n\n 3.) Transfer\n")
if (option == "withdraw"):
	withdraw = input("\n\nHow much would you like to withdraw? $")
	print(account1.withdraw())

























