points = [[0,1],[0,2]]
points = [1,2]

a = 1
b = 1

a+b

if a+b in points:
	print("Yes")


for x in range(0,len(visited)):
		if (a == 0) and (b == 0):
			if (a+1,b == visited[x]):
				vPoint = a+1,b
				possibleV.append(vPoint)
			if (a,b+1 == visited[x]):
				vPoint = a,b+1
				possibleV.append(vPoint)
			lineV = random.randint(0,len(possibleV)-1)
			return possibleV[lineV]

		elif (a == 0) and (b == height-1):
			if (a+1,b == visited[x]):
				vPoint = a+1,b
				possibleV.append(vPoint)
			if (a,b-1 == visited[x]):
				vPoint = a,b-1
				possibleV.append(vPoint)
			lineV = random.randint(0,len(possibleV)-1)
			return possibleV[lineV]

		elif (a == width-1) and (b == 0):
			if (a-1,b == visited[x]):
				vPoint = a-1,b
				possibleV.append(vPoint)
			if (a,b+1 == visited[x]):
				vPoint = a,b+1
				possibleV.append(vPoint)
			lineV = random.randint(0,len(possibleV)-1)
			return possibleV[lineV]

		elif (a == width-1) and (b == height-1):
			if (a-1,b == visited[x]):
				vPoint = a-1,b
				possibleV.append(vPoint)
			if (a,b-1 == visited[x]):
				vPoint = a,b-1
				possibleV.append(vPoint)
			lineV = random.randint(0,len(possibleV)-1)
			return possibleV[lineV]

		else:
			if (a == 0):
				if (a+1,b == visited[x]):
					vPoint = a+1,b
					possibleV.append(vPoint)
				if (a,b-1 == visited[x]):
					vPoint = a,b-1
					possibleV.append(vPoint)
				if (a,b+1 == visited[x]):
					vPoint = a,b+1
					possibleV.append(vPoint)
				lineV = random.randint(0,len(possibleV)-1)
				return possibleV[lineV]

			elif (a == width-1):
				if (a-1,b == visited[x]):
					vPoint = a-1,b
					possibleV.append(vPoint)
				if (a,b-1 == visited[x]):
					vPoint = a,b-1
					possibleV.append(vPoint)
				if (a,b+1 == visited[x]):
					vPoint = a,b+1
					possibleV.append(vPoint)
				lineV = random.randint(0,len(possibleV)-1)
				return possibleV[lineV]

			elif (b == 0):
				if (a+1,b == visited[x]):
					vPoint = a+1,b
					possibleV.append(vPoint)
				if (a-1,b == visited[x]):
					vPoint = a-1,b
					possibleV.append(vPoint)
				if (a,b+1 == visited[x]):
					vPoint = a,b+1
					possibleV.append(vPoint)
				lineV = random.randint(0,len(possibleV)-1)
				return possibleV[lineV]

			elif (b == height-1):
				if (a+1,b == visited[x]):
					vPoint = a+1,b
					possibleV.append(vPoint)
				if (a-1,b == visited[x]):
					vPoint = a-1,b
					possibleV.append(vPoint)
				if (a,b-1 == visited[x]):
					vPoint = a,b-1
					possibleV.append(vPoint)
				lineV = random.randint(0,len(possibleV)-1)
				return possibleV[lineV]

			else:
				if (a+1,b == visited[x]):
					vPoint = a+1,b
					possibleV.append(vPoint)
				if (a-1,b == visited[x]):
					vPoint = a-1,b
					possibleV.append(vPoint)
				if (a,b-1 == visited[x]):
					vPoint = a,b-1
					possibleV.append(vPoint)
				if (a,b+1 == visited[x]):
					vPoint = a,b+1
					possibleV.append(vPoint)
				lineV = random.randint(0,len(possibleV)-1)
				return possibleV[lineV]

#------
	for x in range(0,len(visited)):
		if (a == 0) and (b == 0):
			if (board[b][a+1] == "V"):
				vPoint = a+1,b
				possibleV.append(vPoint)
			if (board[b+1][a] == "V"):
				vPoint = a,b+1
				possibleV.append(vPoint)
			lineV = random.randint(0,len(possibleV)-1)
			return possibleV[lineV]

		elif (a == 0) and (b == height-1):
			if (board[b][a+1] == "V"):
				vPoint = a+1,b
				possibleV.append(vPoint)
			if (board[b-1][a] == "V"):
				vPoint = a,b-1
				possibleV.append(vPoint)
			lineV = random.randint(0,len(possibleV)-1)
			return possibleV[lineV]

		elif (a == width-1) and (b == 0):
			if (board[b][a-1] == "V"):
				vPoint = a-1,b
				possibleV.append(vPoint)
			if (board[b+1][a] == "V"):
				vPoint = a,b+1
				possibleV.append(vPoint)
			lineV = random.randint(0,len(possibleV)-1)
			return possibleV[lineV]

		elif (a == width-1) and (b == height-1):
			if (board[b][a-1] == "V"):
				vPoint = a-1,b
				possibleV.append(vPoint)
			if (board[b-1][a] == "V"):
				vPoint = a,b-1
				possibleV.append(vPoint)
			lineV = random.randint(0,len(possibleV)-1)
			return possibleV[lineV]

		else:
			if (a == 0):
				if (board[b][a+1] == "V"):
					vPoint = a+1,b
					possibleV.append(vPoint)
				if (board[b-1][a] == "V"):
					vPoint = a,b-1
					possibleV.append(vPoint)
				if (board[b+1][a] == "V"):
					vPoint = a,b+1
					possibleV.append(vPoint)
				lineV = random.randint(0,len(possibleV)-1)
				return possibleV[lineV]

			elif (a == width-1):
				if (board[b][a-1] == "V"):
					vPoint = a-1,b
					possibleV.append(vPoint)
				if (board[b-1][a] == "V"):
					vPoint = a,b-1
					possibleV.append(vPoint)
				if (board[b+1][a] == "V"):
					vPoint = a,b+1
					possibleV.append(vPoint)
				lineV = random.randint(0,len(possibleV)-1)
				return possibleV[lineV]

			elif (b == 0):
				if (board[b][a+1] == "V"):
					vPoint = a+1,b
					possibleV.append(vPoint)
				if (board[b][a-1] == "V"):
					vPoint = a-1,b
					possibleV.append(vPoint)
				if (board[b+1][a] == "V"):
					vPoint = a,b+1
					possibleV.append(vPoint)
				lineV = random.randint(0,len(possibleV)-1)
				return possibleV[lineV]

			elif (b == height-1):
				if (board[b][a+1] == "V"):
					vPoint = a+1,b
					possibleV.append(vPoint)
				if (board[b][a-1] == "V"):
					vPoint = a-1,b
					possibleV.append(vPoint)
				if (board[b-1][a] == "V"):
					vPoint = a,b-1
					possibleV.append(vPoint)
				lineV = random.randint(0,len(possibleV)-1)
				return possibleV[lineV]

			else:
				if (board[b][a+1] == "V"):
					vPoint = a+1,b
					possibleV.append(vPoint)
				if (board[b][a-1] == "V"):
					vPoint = a-1,b
					possibleV.append(vPoint)
				if (board[b-1][a] == "V"):
					vPoint = a,b-1
					possibleV.append(vPoint)
				if (board[b-1][a] == "V"):
					vPoint = a,b+1
					possibleV.append(vPoint)
				lineV = random.randint(0,len(possibleV)-1)
				return possibleV[lineV]