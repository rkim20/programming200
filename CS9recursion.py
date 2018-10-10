
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
"""
#Count number of x in a string
#NOT RECURSION FIND SOLUTION ONLINE
def countX(user):
	global count
	user = str(user)

	
	count = 0
	for x in range(len(user)):
		if (user[x] == "x"):
			count += 1
	return(count)
	

	if (len(user))


countX("xxx")
print(count)
"""
#------------------------------------------------------------
"""
#NOT RECURSION FIND SOLUTION ONLINE
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
#------------------------------------------------------------
#Recursion - without a loop and calls on itself within the function


#Tower of Hanoi

def moves(n, left):
	if (n == 0):
		return #basically break

	moves(n-1,not left)

	if  left:
		print (str(n)+' left')

	else:
		print (str(n)+' right')
	moves(n-1,not left)



moves(3, True)

"""
Trace
If the moves function is called with the parameters (3, True), the program will pass over the first if statement as n is not 0. It'll hit the moves function with parameters (n-1, not left). The function will start over with parameters (2, False). Again, it'll come back to the same point where it resets. When it comes back again with parameters (1, True), the "n-1" becomes 0 and the first if statement takes effect. It returns nothing and then the (1, True) follows into the second if statement where it prints "1 left".

Explanation
I do not fully understand the code, but what I think is happening is that the moves function that is called in the function itself is reducing the number to 1 in order to get the smallest ring out of the way. Then, from there, it starts moving the next greatest numbers to remove and organize them, finally reaching the greatest number and moving it. It also places the rings in different places so that open spaces for bigger rings can exist.

"""










