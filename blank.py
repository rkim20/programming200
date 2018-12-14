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
height = 7
width = 7

'''
board = []
board = [["#"]*width for x in range(height)]


for y in range (1, height-1):
	for x in range(1, width-1):
		print(board[y][x], end = " ")
	print("")
'''

'''
--------------------------------------
for i in range (width):
	print("#", end = "")

print("\n")

for i in range (width-2):
	print("#     #")

for i in range (width):
	print("#", end = "")
--------------------------------------
'''

'''
--------------------------------------
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
--------------------------------------
'''

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











