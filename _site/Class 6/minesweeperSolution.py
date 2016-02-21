from minesweeperHelper import * # gives access to helper functions:

# Helper Functions:
	# createBoard(rows, columns)
	# putBomb(board,row,column)
	# loopThroughBoardAndDo(board, function_on_each_element, function_after_each_row) - takes a board and two functions, 
	# 						the first functions gets called on each element with three arguements, the board, row and columns, the second, gets 
	#						called on each row, and has two arguements, the board and row
	#						ex: loopThroughBoardAndDo(board, putBomb , None) will place put a bomb at each place
	# putBombsInBoard(board, bombs)
	# printBoard(board)
	# printPlayBoard(board,bombs)
	# playMineSweeper(rows, columns, bombs)
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
	loopThroughBoardAndDo(board,function_on_each_element=putNumber)
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
playMineSweeper(4,4,2)
# board = createBoard(4,4)
# putBombsInBoard(board,7)
# printBoard(board)
# print("-----------")
# fillInBoard(board)