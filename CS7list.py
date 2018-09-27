import random as r

#empty list
a = []


#adds value to the end of the list
a.append(4)
a.append(5)
a.append(3)

#adds value to the front or to a given position
a = [1] + a
a.insert(0,1) #position, value

#prints only certain values
print (a[0], a[4])

#prints the whole list
print(a)


#-------------------------------------------------------------------------

b = [1, 2, 3, 4, 5]

#removes by value not by position
b.remove(1)

#removes by position not by value
del b[0]

#takes last value of the list and prints the value once
print(b.pop())

#prints the last value in the list because it prints the length-1 which is the last value
print (b[len(b)-1])

#prints last thing is in the list
print(b[-1])

#prints second last thing in the list
print(b[-2])

#swap
c = 5
d = 7

c, d = d, c

temp = c
c = d
d = temp


#for loops
f = []

#range - 0 is included; 101 is not included; add 7 from starting number (step)
for x in range(0,101,7):
	f.append(x)
print(f)

#---------------------------------------------------------------------------

g = []
for x in range(10):
	g.append(r.randrange(10))

#sorts from least to greatest
g.sort()
print(g)

#shows what a sorted list would look like but doesn't actually rearrange the numbers or values
g = sorted(g)
print(g)

#---------------------------------------------------------------------------

#There is a list of names. Create a program to remove all the words that start with the letter 'a'.

nameList = ['Ashley', 'Albert', 'George', 'Abby', 'Ryan']

for x in range(len(nameList)):
	if 'a' in nameList:
		nameList.remove(x)


print (nameList)









