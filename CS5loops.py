

while True:
	try:
		num = int(input("Pick a number between 1 and 5: "))
		while num < 1 or num > 5:
			num = int(input("That's not in the right range. Please choose a number between 1 and 5: "))
		break

	except ValueError or NameError:
		print("That's not a number. Try again.")




"""
while num > count:
	print ("Hi")
	count+=1
"""