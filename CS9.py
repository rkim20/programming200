
"""
def add(x,y):
	return x+y
	#nothing happens after the return function


print(add(5,6))

x = add(7,3)
"""
#------------------------------------------------------------
"""
Factorial
def factorial(n):
	if (n == 0) or (n == 1):
		return(1)

	else:
		return(n*factorial(n-1))


print(factorial(998))
"""
#------------------------------------------------------------

#Count number of x in a string
def countX(user):
	global count
	user = str(user)

	"""
	count = 0
	for x in range(len(user)):
		if (user[x] == "x"):
			count += 1
	return(count)
	"""

	if (len(user))


countX("xxx")
print(count)

#------------------------------------------------------------
"""
#Count number of 8s in a string
def count8(number):
	global count

	number = str(number)

	count = 0
	for x in range(len(number)):
		if (number[x] == "8"):
			count += 1
			if (number[x] == "8") and (number[x+1] == "8"):
				count += 1
	return(count)


count8(4889480)
print(count)
"""
#------------------------------------------------------------
"""
#Given two numbers, use euclid's algorithm to calculate the gcd for those two numbers
def gcd(a, b):
	a = int(a)
	b = int(b)

	if (b > a):
		c = a
		a = b
		b = c

	if (a == 0) and (b != 0):
		return(b)

	elif (a != 0) and (b == 0):
		return(a)

	else:
		remainder = a%b
		a = b
		b = remainder
		return(gcd(a,b))



print(gcd(192,270))
"""


#Recursion - without a loop and calls on itself within the function





