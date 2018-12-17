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