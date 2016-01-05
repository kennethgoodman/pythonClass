def printBoard(board):
	print("--------")
	for row in range(4):
		for column in range(4):
			print(str(board[row][column]),end=" ")
		print("")
def createBoard():
	board = [[0]*4 for i in range(4)]
	for row in range(4):
		for column in range(4):
			board[row][column] = row*4 + column + 1
	board[3][3] = "_"
	return board
def move(board,row,column,x,y):
	try:
		if((abs(x) != 1 and abs(y) !=1) or abs(x) > 1 or abs(y) > 1 or (abs(x) == 1 and abs(y) == 1)):
			raise NameError("")
		if(row+y >= 0 and column+x >=0):
			temp = board[row][column]
			board[row][column] = board[row+y][column+x]
			board[row+y][column+x] = temp
		else:
			raise NameError("Can\'t move like that")
	except (IndexError, NameError):
		raise NameError("Can\'t move like that")
def getMove():
	direction = input("Left (a),right (d), up (w) or down (s): ").lower()
	switcher = {
		'w': {'x':0,'y':-1},
		'a': {'x':-1,'y':0},
		's': {'x':0,'y':1},
		'd': {'x':1,'y':0},
	}
	return switcher.get(direction, {'x':0,'y':0},)
def win(board):
	for row in range(4):
		for column in range(4):
			if(board[row][column] != row*4 + column + 1 and board[row][column] != "_"):
				return False
	return True
def randomStart():
	a = [i for i in range(1,16)]
	a.append("_")
	import random
	return [[a.pop(random.randrange(len(a))) for i in range(4)] for j in range(4)]
printBoard(randomStart())
def playFifteen():
	board = createBoard()
	printBoard(board)
	row = column = 3 # starting place for empty space
	playingGame = True
	while playingGame:
		currentMove = getMove()
		try:
			move(board,row,column, currentMove['x'], currentMove['y'])
			row += currentMove['y']
			column += currentMove['x']
			printBoard(board)
		except NameError as e:
			print(e)
		if(win(board)):
			playingGame = False
			print("You won!")
#playFifteen()
