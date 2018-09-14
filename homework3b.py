import sys

number1 = sys.argv[1]
number2 = sys.argv[2]
number3 = sys.argv[3]

int(number1)
int(number2)
int(number3)

if (number1 < number2) and (number2 < number3):
	print("True")
elif (number1 > number2) and (number2 > number3):
	print("True")
else:
	print("False")


#https://stackoverflow.com/questions/1075652/using-the-and-and-not-operator-in-python
#This source helped me understand the 'and' statement which was && in processing