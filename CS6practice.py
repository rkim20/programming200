"""
#Fibonachi
import sys

num = [1,1,2]
number = float(sys.argv[1])

while len(num) < number:
	num.append(num[len(num)-1]+num[len(num)-2])

print (num)
"""

#Binary -> Decimal