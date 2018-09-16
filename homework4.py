import sys

grade = float (sys.argv[1])

if (grade < 0) or (grade > 5):
	print ("Input a number between 5 and 0")
elif (grade >= 4.85):
	print ("A+")
elif (grade >= 4.7):
	print ("A")
elif (grade >= 4.5):
	print ("A-")
elif (grade >= 4.2):
	print ("B+")
elif (grade >= 3.85):
	print ("B")
elif (grade >= 3.5):
	print ("B-")
elif (grade >= 3.2):
	print ("C+")
elif (grade >= 2.85):
	print ("C")
elif (grade >= 2.5):
	print ("C-")
elif (grade >= 2):
	print ("D+")
elif (grade >= 1.5):
	print ("D")
elif (grade >= 1.0):
	print ("D-")
else:
	print ("F")