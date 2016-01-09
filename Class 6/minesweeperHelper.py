import random #for random numbers
def createBoard(rows, columns):
	if rows <= 0: # if user puts bad input
		raise NameError("need to have more than zero rows")
	return [["-"]*columns for i in range(rows)] #return 2d array with all '-'
def putBomb(board,row,column):
	board[row][column] = "*"
def loopThroughBoardAndDo(board, function_on_each_element, function_after_each_row):
	rows = len(board[0])  #is this really columns?, test this
	for row in range(len(board)):
		for column in range(rows):
			if(function_on_each_element): #if it exists
				function_on_each_element(board,row ,column)
		if(function_after_each_row):
			function_after_each_row(board,row)
def putBombsInBoard(board, bombs):
 	if bombs >= len(board)*len(board[0]): # if the user wants as many bombs as their are spaces or more, fill the board with bombs
 		loopThroughBoardAndDo(board, putBomb , None) 
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
		lambda board,row,column: print(board[row][column],end=" "), # function to print each element without a new line
		lambda a,b: print("\n")) 								   # function to print a new line at the beggining of each row
