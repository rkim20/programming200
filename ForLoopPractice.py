''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables mentioned in the description are declared and initialized; however, feel free to use additional variable as necessary (please avoid extra variables, though; don't use them unless you must to store a required value or simplify your code.) Write your solution below the commented description.
'''
 
''' 1. 
   Write a for loop that will print out all the integers from 0-4 in ascending order. 
'''
for i in range(5):
    print(i)
 
''' 2. 
   Write a for loop that will print out all the integers from 0-4 in descending order.
'''
x = 4
for i in range(5):
  print(x)
  x -= 1
 
 
''' 3. 
   Write a for loop that will print out all the integers from 5-15 in descending order.
'''
x = 15
for i in range(11):
  print(x)
  x -= 1
 
 
''' 4. 
   Write a for loop that will print out all the integers from -5 to 5 in ascending order.
'''
for i in range(11):
  print(i-5)
 
 
''' 5. 
   Write two for loops that will both print out odd numbers from 25 to 49. The loops themselves must be different, but they will have the same output.
'''
 
 
''' 6. 
   Write a for loop that prints out the squares of the numbers from 1 to 10. ie 1, 4, 9, 16, ... 100
'''
x = 1
for i in range(10):
  y = x**2
  x += 1
 
 
''' 7. 
   Write while loops that do the same thing as numbers 1-6.
'''
# 1
 
 
# 2
 
 
# 3 
 
 
# 4
 
  
# 5
 
 
# 6
 
 
 
''' 8. 
   A number starts at 4 and increases by one every day after the day it was created. Write a loop and use the variable days (int) that will print out how many days it will take for number to reach 57. 
'''
x = 4
for i in range(53):
  x += 1
  days = 57 - x
  print(days)
 
 
''' 9. 
   A girl in your class has jellybeans in a jar. The number of jellybeans is stored in int beans. Every day she shares one jellybean with every student in the class, and she herself takes two. The number of students in the class is held in variable students (int). Write a loop that determines how many days it will take for her to run out of jellybeans. You can store the result in variable numDays (int).
'''

 
 
''' 10. 
   Today is the 14th of December. Vacation starts on firstDayOfVacation (int). Assuming your vacation starts in December, write a loop that will count down the number of days until your vacation starts. It's output should be something like: "10 days until vacation!" "9 days until vacation!" ... "1 day until vacation!" "Vacation has arrived!"
'''
x = 14
for i in range(6):
  days = 19 - x
  if days == 0:
    print("Vacation!")
  else:
    print(days + " days until vacation!")
 
 
''' 11. 
   Write a loop that will calculate n factorial. The sum should be stored in result (int).
'''

 
 
''' 12. 
   A flying car can travel an average of 96mph. Write a loop that will determine how long it will take you (to the nearest quarter hour) to get to your destination if you were to travel by flying car. The distance to your destination is stored in distance (int).
'''
speed = 96
while (distance > 0):
  time = distance/speed
  time = (time/15)//1
  time = time*15
 
 
''' 13.  
   Write a loop that, given a number, n, will determine the value of n to the power of b. Store the result in variable exponent (int). 
'''
 
 
 
''' 14. 
   Write a loop that will print out all the letters of the alphabet.
'''
alphabet = abcdefghijklmnopqrstuvwxyz
for x in range(26):
  print(alphabet[x])

 
''' 15. 
   Now write a loop that will print out "A is a vowel." "B is a consonant." "C is a consonant." and so on. 
'''
 
 
 
''' 16. 
   Write code that will produce the following output: 
   122333444455555666666777777788888888999999999
'''
for x in range(9):
  y = x+1
  for i in range(y):
    list.append(y)
 
 
''' 17. 
   Write a loop that will print out the decimal equivalents of 1/2, 1/3, 1/4, 1/5, 1/6, ... 1/20. The output for each iteration should look like:
   "1/2 = .5" "1/3 = .666666666667" etc.
'''
 
 
 
''' 18. 
   Write a loop that determines the sum of all the numbers from 1-100, as well as the average. Store the sum in variable total (int) and the average in variable avg (float).
'''
for i in range(100):
  x = i+1
  total += x
  average = total/x
 
 
''' 19. 
   A friend tells you that PI can be computed with the following equation:
   PI = 4 * (1-1/3+1/5-1/7+1/9-1/11+1/13-1/15...)
   Write a loop that will calculate this output for n-iterations of the pattern (n being an int), that could help you determine if your friend is right or wrong.
'''
 
 
 
''' 20. 
   A mother rabbit can have a litter of rabbits every month. In the litter, the number of rabbits can vary from 1 to 14 babies per litter, half of which are females. Rabbits can start reproducing at 6 months, so let's add all the new rabbits from the year to the reproductive pool at the end of each year (when their average age is 6 months). Write a simulation that will show how many rabbits will exist at the end of 5 years, starting with just one mother rabbit. 
'''
rabbitsf = 1
rabbits = 1
total = 1
while (time < 60):
  for i in range(rabbitsf):
    babies = random.randint(1,14)
    total += babies
    newF = babies//2
    timer.append(time)
    for y in range(len(timer)):
      if (timer[y] == time-6):
        rabbitsF += newF


  time += 1
 
''' 21. 
   Write some code that will run the rabbit simulation above 1000 times, to help determine what we can expect on average.
'''
 
 
 
''' 22. 
   Write a loop which prints the numbers 1 to 110, 11 numbers per line. The program shall print "Coza" in place of the numbers which are multiples of 3, "Loza" for multiples of 5, "Woza" for multiples of 7, "CozaLoza" for multiples of 3 and 5, and so on. Sample output:
   1 2 Coza 4 Loza Coza Woza 8 Coza Loza 11 
   Coza 13 Woza CozaLoza 16 17 Coza 19 Loza CozaWoza 22 
   23 Coza Loza 26 Coza Woza 29 CozaLoza 31 32 Coza
   ......
'''
width = 11
height = 10

board = []
board = [[0]*width for x in range(height+1)]

x = 1

for i in range(height):
  for j in range(width):
    board[i][j] = x
    x = x + 1


for i in range(height):
  for j in range(width):
    if (board[i][j]%3 == 0) and (board[i][j]%5 == 0):
      board[i][j] = "CozaLoza"
    elif (board[i][j]%3 == 0) and (board[i][j]%7 == 0):
      board[i][j] = "CozaWoza"
    elif (board[i][j]%5 == 0) and (board[i][j]%7 == 0):
      board[i][j] = "LocaWoza"
    elif (board[i][j]%3 == 0):
      board[i][j] = "Coza"
    elif (board[i][j]%5 == 0):
      board[i][j] = "Loza"
    elif (board[i][j]%7 == 0):
      board[i][j] = "Woza"


for i in range (height):
  for j in range (width):
    print(board[i][j], end = " ")
  print("")

 
 
''' 23.
   Write code that will print out a times-table for practice and reference. It should look like this:
    * |  1  2  3  4  5  6  7  8  9
    -------------------------------
    1 |  1  2  3  4  5  6  7  8  9
    2 |  2  4  6  8 10 12 14 16 18
    3 |  3  6  9 12 15 18 21 24 27
    4 |  4  8 12 16 20 24 28 32 36
    5 |  5 10 15 20 25 30 35 40 45
    6 |  6 12 18 24 30 36 42 48 54
    7 |  7 14 21 28 35 42 49 56 63
    8 |  8 16 24 32 40 48 56 64 72
    9 |  9 18 27 36 45 54 63 72 81
'''
 
 
 
''' 24. 
   Write code that will produce each of these visual outputs:
   # # # # # # #    # # # # # # #    # # # # # # #
   #           #      #       #      # #       # #
   #           #        #   #        #   #   #   #
   #           #          #          #     #     #
   #           #        #   #        #   #   #   #
   #           #      #       #      # #       # #
   # # # # # # #    # # # # # # #    # # # # # # #
'''

width = 7
height = 7

for i in range (width):
  print("#", end = "")

print("\n")

for i in range (width-2):
  print("#     #")

for i in range (width):
  print("#", end = "")

--------------------------------

for i in range (width):
  print("#", end = "")

print("\n")

print(" #   # ")

print("  # #  ")


print("   #   ")


print("  # #  ")


print(" #   # ")

for i in range (width):
  print("#", end = "")

--------------------------------

for i in range (width):
  print("#", end = "")

print("\n")

print("##   ##")

print("# # # #")


print("#  #  #")


print("# # # #")


print("##   ##")

for i in range (width):
  print("#", end = "")

  
 
''' 25. 
   Write code that will extract each digit from an int, in the reverse order. For example, if the int is 15423, the output shall be "3 2 4 5 1", with a space separating the digits.
   Hint: Use n % 10 to extract the least-significant digit; and n = n / 10 to discard the least-significant digit.
'''
 
 
 
''' Sources
   http://www.bowdoin.edu/~ltoma/teaching/cs107/fall05/Lectures-Handouts/for.pdf
   http://www.ntu.edu.sg/home/ehchua/programming/java/j2a_basicsexercises.html
'''