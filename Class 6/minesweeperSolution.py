from minesweeperHelper import * # gives access to helper functions:

#Helper Functions:
# createBoard(rows, columns)
# putBomb(board,row,column)
# loopThroughBoardAndDo(board, function_on_each_element, function_after_each_row) - takes a board and two functions, 
# 						the first functions gets called on each element with three arguements, the board, row and columns, the second, gets 
#						called on each row, and has two arguements, the board and row
#						ex: loopThroughBoardAndDo(board, putBomb , None) will place put a bomb at each place
# putBombsInBoard(board, bombs)
# printBoard(board)
def fillInBoard(board):
	def getNumberOfBombsSurrounding(board, row, column):
		bombs = 0
		directions = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]
		for direction in directions:
			x,y = direction
			try: #protect against index out of range
				if(board[x+row][y+column] == "*" and x+row >= 0 and y+column >= 0):
					bombs += 1
			except IndexError:
				continue 
		return bombs
	def putNumber(board,row,column):
		if(board[row][column] != "*"):
			board[row][column] = getNumberOfBombsSurrounding(board,row,column)
	loopThroughBoardAndDo(board,putNumber, None)
	# The board should be filled so that each element that is not a * has the number of * directly adjacent in the four cardinal directions
	# and the four diagonals
	# Implement this function to have the board print out the correct number in each box
	# IE: 	* - -
	#	 	- * -
	#		- - -
	#		- - *
	# Should fill the board so that the board looks like:
	#		* 2 1
	#		2 * 1
	#		1 2 1
	#		0 1 *
	return
def printPlayBoard(board,bombs):
	print("Bombs: " + str(bombs))
	for i in range(len(board[0])):
		print(str(i), end=" ")
	print("")
	for i in range(len(board[0])*2):
		print("-",end="")
	print("")
	loopThroughBoardAndDo(board, lambda board,row,column: print(board[row][column],end=" ") , lambda board,row: print("|" + str(row)))
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
			
playMineSweeper(4,4,2)
# board = createBoard(4,4)
# putBombsInBoard(board,7)
# printBoard(board)
# print("-----------")
# fillInBoard(board)