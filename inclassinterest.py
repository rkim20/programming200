'''
import sys
import math

p = sys.argv[1]
r = sys.argv[2]
t = sys.argv[3]

r = float(r)
r = r/100

p = float(p)
r = float(r)
t = float(t)

interest = p*(math.e)**(r*t)

print ("Total Money After Interest:", interest)
'''

answer = input("What is the weather like? ")
if (answer == "Rainy" or answer == "rainy"):
	print("I hope you brought your umbrella!")
else:
	print ("Nice!")