import random

class Account():

	#Constructor
	def __init__(self, balance):
		self.balance = balance
		self.pinNumber = pinNumber
		self.accountNumber = random.randint(10000,99999)
		#self.working


	#Methods
	def openAccount(self):
		#self.accountNumber = random.randint(10000,99999)

		status = "Balance: $" + self.balance + "\nPin Number: " + self.pinNumber + "\nAccount Number: " + str(self.accountNumber)

		return status



	def withdraw(self):
		self.balance = int(self.balance)
		self.balance -= int(withdraw)

		status = "You withdrew $" + str(withdraw) + ". Your account balance is now $" + str(self.balance)

		return status

	def deposit(self):
		self.balance = int(self.balance)
		self.balance += int(deposit)

		status = "You deposited $" + str(deposit) + ". Your account balance is now $" + str(self.balance)

		return status



#----------------------------------------------------------------------------------------------

balance = input("How much money would you like to deposit into this account? ")
pinNumber = input("\n\nWhat would you like your pin number to be? ")

account1 = Account(balance)

print (account1.openAccount())

#User Actions
option = input("What would you like to do today?\n\n 1.) Withdraw\n\n 2.) Deposit\n\n 3.) Transfer\n")
if (option == "withdraw") or (option == "1") or (option == "Withdraw"):
	withdraw = input("\n\nHow much would you like to withdraw? $")
	print(account1.withdraw())

elif (option == "2") or (option == "deposit") or (option == "Deposit"):
	deposit = input("\n\nHow much would you like to deposit? $")
	print(account1.deposit())
























