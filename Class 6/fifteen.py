def printBoard(board):
	print("--------")
	for row in range(4):
		for column in range(4):
			print(str(board[row][column]),end=" ")
		print("")
def createBoard():
	board = [[0]*4 for i in range(4)] #init board with a 2d array of 0s
	for row in range(4):
		for column in range(4):
			board[row][column] = row*4 + column + 1 
                      # initialize each entry to correct entry 
	board[3][3] = "_" #start empty at 3,3
	return board
def move(board,row,column,x,y):
	try:
               # check if the user wants to move either in the X or y direction, 
               # not one space 
               # or if the user wants to move more than one space
               # or if the user wants to move diagonally 
               # we want the movement to be one of four options: 
               # (+/-1,0) or (0,+/-1)
               # change this to be quicker and more readable 
		if((abs(x) != 1 and abs(y) !=1) or abs(x) > 1 or abs(y) > 1 or (abs(x) == 1 and abs(y) == 1)):
			raise NameError("") #if illegal, throw error
		if(row+y >= 0 and column+x >=0): #if moving in the board
			temp = board[row][column]
			board[row][column] = board[row+y][column+x]
			board[row+y][column+x] = temp
		else: #trying to move outside board
			raise NameError("Can\'t move like that")
	except (IndexError, NameError): #error was thrown for
               # illegal move or outside bounds
		raise NameError("Can\'t move like that")
def getMove():
	direction = input("Left (a),right (d), up (w) or down (s): ").lower() # get direction
       #four possible directions
       #TODO: move outside func to make more polymorphic 
	switcher = {
		'w': {'x':0,'y':-1},
		'a': {'x':-1,'y':0},
		's': {'x':0,'y':1},
		'd': {'x':1,'y':0},
	}
	return switcher.get(direction, {'x':0,'y':0}) #defualt is no movement
def win(board):
	for row in range(4):
		for column in range(4):
			if(board[row][column] != row*4 + column + 1 and board[row][column] != "_"): #if it's not the empty or the correct number
                      # move to one for loop 1->15 for efficiency 
				return False
	return True #if it got this far, it's a win
def randomStart():
	a = [i for i in range(1,16)]
	a.append("_")
	import random
	return [[a.pop(random.randrange(len(a))) for i in range(4)] for j in range(4)]
        # return a 2d array with a random element from a inside it, pop after inserting
#printBoard(randomStart())
def playFifteen():
	board = createBoard()
	printBoard(board)
	row = column = 3 # starting place for empty space
       # row and column keep track of the empty space
	playingGame = True
	while playingGame:
		currentMove = getMove()
		try:
			move(board,row,column, currentMove['x'], currentMove['y'])
                      #move the empty square
			row += currentMove['y'] 
			column += currentMove['x']
			printBoard(board)
		except NameError as e: #if illegal move
			print(e) #print error
		if(win(board)): #game is won
			playingGame = False #will end loop
			print("You won!")
#playFifteen()
