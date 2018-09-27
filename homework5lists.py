
#Ryan Kim
#Homework for Friday, September 28th, 2018

#https://docs.python.org/2/howto/sorting.html - I used this source to help with reversing the sort() function.

#I found that using for loops was extremely difficult for me. The range part of it confused me the most.

#-----------------------------------------------------------------------------------

"""
#1.) This problem was to choose ask the user to input a number and for that number to be added to a list of 15 random numbers between 0-100. After that, the list had to be put into descending order.

import random

list = []

for x in range(15):
	list.append(random.randrange(100))

number = input("Choose a number to be in the list ")
number = int(number)

list.append(number)

list.sort(reverse = True)

print (list)
"""

#-----------------------------------------------------------------------------------

"""
#2.) This problem was to have the user input a base and an exponent and have a list printed out. The first number in the list would be the base to the exponent of 0. The second would be the base to the power of 1. This would go on until the last number was the base to the power of the exponent that the user input at the beginning.

base = input("Input a number as your base ")
exponent = input("Input a number as your exponent ")

base = int(base)
exponent = int(exponent)

list = []

y = 0

for x in range (exponent+2):
	list.append(base**x)

print (list)
"""

#-----------------------------------------------------------------------------------

"""
#3.) This problem was to have the user input 10 different numbers and have a list show the numbers in both descending and ascending order. Then, the program would have to print the sum of the numbers.

list = []

while True:
	try:
		num1 = input("Input 10 integers (hit the enter key after each number) ")
		num2 = input()
		num3 = input()
		num4 = input()
		num5 = input()
		num6 = input()
		num7 = input()
		num8 = input()
		num9 = input()
		num10 = input("This is the final number you have to input! ")

		num1 = int(num1)
		num2 = int(num2)
		num3 = int(num3)
		num4 = int(num4)
		num5 = int(num5)
		num6 = int(num6)
		num7 = int(num7)
		num8 = int(num8)
		num9 = int(num9)
		num10 = int(num10)
		break
	except ValueError:
		print("You didn't input all numbers!")

list.append(num1)
list.append(num2)
list.append(num3)
list.append(num4)
list.append(num5)
list.append(num6)
list.append(num7)
list.append(num8)
list.append(num9)
list.append(num10)

list.sort()
print (list)

list.sort(reverse = True)
print (list)

sum = 0

for x in range (10):
	sum = sum + list[x]

print(sum)
"""




































