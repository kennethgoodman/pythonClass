import random #for random numbers
def createBoard(rows, columns):
	if rows <= 0: # if user puts bad input
		raise NameError("need to have more than zero rows")
	return [["-"]*columns for i in range(rows)] #return 2d array with all '-'
def putBomb(board,row,column):
	board[row][column] = "*"
#TODO change to named optional arguments
def loopThroughBoardAndDo(board, function_on_each_element=None, function_after_each_row=None):
	rows = len(board[0])  #is this really columns?, test this
	for row in range(len(board)):
		for column in range(rows):
			if(function_on_each_element): #if it exists, maybe change to callable(function...)
				function_on_each_element(board,row ,column)
		if(function_after_each_row):
			function_after_each_row(board,row)
def putBombsInBoard(board, bombs):
 	if bombs >= len(board)*len(board[0]): # if the user wants as many bombs as their are spaces or more, fill the board with bombs
 		loopThroughBoardAndDo(board, function_on_each_element=putBomb) 
 	else:
 		bombsLeftToPlace = float(bombs) #convert to float so that we can do fractional math with it
 		columns = len(board[0])
 		rows = len(board)
 		row = column = 0
 		while bombsLeftToPlace > 0:
 			if(random.random() > (bombsLeftToPlace/bombs - .1) and board[row][column] != "*"): #math formula to place bombs pseudo randomly 
 				board[row][column] = "*"
 				bombsLeftToPlace = bombsLeftToPlace - 1.0
 			column = (column + 1)%columns #increment the column
 			if column == 0: #if on the first column
 				row = (row+1)%rows
def printBoard(board):
	loopThroughBoardAndDo(board,
		function_on_each_element=lambda board,row,column: print(board[row][column],end=" "), # function to print each element without a new line
		function_after_each_row=lambda a,b: print("\n")) 								   # function to print a new line at the beggining of each row
def printPlayBoard(board,bombs):
	print("Bombs: " + str(bombs))
	for i in range(len(board[0])):
		print(str(i), end=" ")
	print("")
	for i in range(len(board[0])*2):
		print("-",end="")
	print("")
	loopThroughBoardAndDo(board, 
		function_on_each_element=lambda board,row,column: print(board[row][column],end=" "), 
		function_after_each_row= lambda board,row: print("|" + str(row)))
def playMineSweeper(rows, columns, bombs):
	fullBoard = createBoard(rows, columns)
	putBombsInBoard(fullBoard, bombs)
	fillInBoard(fullBoard)
	#printBoard(fullBoard) 	# for testing
	#print("")				# for testing
	playBoard = createBoard(rows, columns)
	playingGame = True
	printPlayBoard(playBoard,bombs)
	totalFound = 0
	while playingGame:
		############################## Get Input ##############################
		row = int(input("enter the row: "))
		column = int(input("enter the column: "))
		############################## Get Input ##############################
		
		if(playBoard[row][column] == "-"):
			element = playBoard[row][column] = fullBoard[row][column]
			totalFound += 1
		else:
			continue
		if element == "*": #if bomb
			print("You lost")
			playingGame = False
		else: #if not bomb
			if element == 0: #if zero bombs surrounding
				def allDirectionsDo(totalFound,ifFunc, doFunc):
					directions = [(-1,1), (0,1), (1,1),
								  (-1,0),        (1,0),
								  (-1,-1),(0,-1),(1,-1)]
					for direction in directions:
						x,y = direction
						try: #protect against index out of range
							if(ifFunc(x,y)):
								doFunc(totalFound,x,y)
						except IndexError:
							continue 
					return totalFound
				def setBoard(totalFound,x,y):
					playBoard[x+row][y+column] = fullBoard[x+row][y+column]
					#if(playBoard[x+row][y+column] == "0"):
					#	totalFound = allDirectionsDo(totalFound, lambda a,b: (a+x+row >= 0 and b+y+column >= 0 and playBoard[a+x+row][b+y+column] == "-"), setBoard)
					totalFound += 1
				totalFound = allDirectionsDo(totalFound, lambda x,y: (x+row >= 0 and y+column >= 0 and playBoard[x+row][y+column] == "-"), setBoard)		
			printPlayBoard(playBoard,bombs)
		if totalFound == rows*columns - bombs:
			print("You\'ve won!")
			playingGame = False
			
