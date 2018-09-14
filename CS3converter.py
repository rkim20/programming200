import math
import random

"""
# currency convertor
dollars = input("Dollars to yen: ")
won = input("Dollars to won: ")

result = float(dollars) * 111.47
result2 = float(won) * 1000

print("Yen:",result)
print("Won:", result2)
"""

#Prints a number between 101 and 0 that is separated by 10 (10,20,30...)
random.randrange(0,101,10)

#x = random.randrange(0,2*math.pi)
#y = random.randrange(0,2*math.pi)

theta = random.random()*math.pi*2
trigResult = math.sin(theta)**2 + math.cos(theta)**2
print(trigResult)