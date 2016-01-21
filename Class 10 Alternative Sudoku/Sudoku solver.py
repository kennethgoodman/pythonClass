# coding: utf-8
class Board (object):
	#change dim to dimensions
	#change board to sudokuboard and create new parent board class. this way we can have many solutions with just one implemented placeable() which as a parent always returns true. this will give an indentity board at first. 
	def __init__(self, dim):
		self.dim = dim
		self.sudokuBoard = []
		for i in range(dim):
			self.sudokuBoard.append([])
			for j in range(dim):
				self.sudokuBoard[i].append(Square())
	def __str__(self):
		ret = ""
		for i in range(self.dim):
			for j in range(self.dim):
				#should we put logic to replace zeros with underscores or spaces?
				ret += str(self.sudokuBoard[i][j]) + " "
				if j % 3 == 2:
					ret += ' '
			if i % 3 == 2:
				ret += '\n'
			ret += "\n"
		return ret
	def setboard(self, newBoard):
		self.sudokuBoard = newBoard
	def setSquare(self, row, column, num):
		self.sudokuBoard[row][column].setSquare(num)
	def getDim(self):
		return self.dim
	def getSquare(self,row,column):
		return self.sudokuBoard[row][column].getNum()
	def hasNum(self, row, column):
		return self.getSquare(row,column)
	def getRow(self, row):
		return [self.getSquare(row,index) for index in range(9)]
	def getColumn(self, column):
		return [self.getSquare(index,column) for index in range(9)]
	def placeable(self,row,column, num):
		def checkLine(line, index,num):
			for i in range(9):
				if i != index and num == line[i]:
					return False
			return True
		def checkRow(row,num):
			if checkLine(self.getRow(row), column,num):
				return True
			return False
		def checkColumn(column,num):
			if checkLine(self.getColumn(column), row,num):
				return True
			return False
		def checkGrid(row,column,num):
			rowStart = (row/3)*3
			columnStart = (column/3)*3
			for i in range(rowStart,rowStart+3):
				for j in range(columnStart,columnStart+3):
					if num == self.getSquare(i,j) and row != i and j != column:
						return False
			return True
		return checkRow(row,num) and checkColumn(column,num) and checkGrid(row,column,num)
		
class Square (object):
	def __init__(self, num=0):
		self.number = num
		self.possible = []
	def __str__(self):
		return str(self.number)
	def setSquare(self,num):
		self.number = num
	def getNum(self):
		return self.number
	def setPossible(self, possible):
		self.possible = possible

def getNextEmpty(board,row,column):
		for i in range(row*9 + column, 81): #from this grid until the end
			j = i % 9 
			i = i / 9 
			if board.getSquare(i,j) == 0: #if a number hasnt been placed here
				return i,j
		return -1,-1	
def solve(board):
	'''
	This function takes a board and will try and fill the board with the first chronological solution. 
	
	for example: with the class above for sudoku board and the function placeable() for the Board class, it will place numbers in available spots (given from getNextEmpty()) until there are no more empty squares. 
	
	
	backtracking solution:
		
	while we are still solving:
		if the current square were at is at or below 8
			increment the square
			if the increment was placeable()
				add this position to our stack
				get the next empty square
					if none
						exit
		else
			set square to zero
			go to last placed square and redo
			
	'''
	#TODO test this on non working boards/unsolveae boards
	#TODO change the variable names to be more english like
	#TODO add an optional debug arg
	stack = [] # represents the positions of last placed numbers
	solveable = True
	row = column = 0
	while solveable: #id like to change solveable to stillsolving or more english like grammer
		current = board.getSquare(row,column)
		if current+1 <= 9: #change to more polymorphic condition, maybe like if board.aboveLimits(current)
			board.setSquare(row,column,current +1) #change to more polymorphic increment. maybe like board.nextpossible
			#print(board)
			if board.placeable(row,column,current +1):
				stack.append((row,column))
				row, column = getNextEmpty(board,row,column) #maybe change to a class function instead
				if (row, column) == (-1,-1): #out of board. means we finished
					solveable = False 
			else:
				continue #not placeable try next num
		else: 
			board.setSquare(row,column,0)
			row, column = stack.pop() #go to last placed spot
	return board

#example
print("this example will give you the first chronologically possible sudoku board. then solve an already made one. \n")
b = Board(9)
print(solve(b))

print('the unfinished one:\n')
b = Board(9)
b.setSquare(0,2,9), b.setSquare(0,3,7)

b.setSquare(1,0,5), b.setSquare(1,5,2), b.setSquare(1,6,7), b.setSquare(1,8,9)

b.setSquare(2,0,8),b.setSquare(2,4,1), b.setSquare(2,8,6)

b.setSquare(3,2,1), b.setSquare(3,3,6), b.setSquare(3,6,4), b.setSquare(3,8,5)

b.setSquare(4,4,4)

b.setSquare(5,0,7), b.setSquare(5,2,6), b.setSquare(5,5,8), b.setSquare(5,6,2)

b.setSquare(6,0,4), b.setSquare(6,4,9), b.setSquare(6,8,8)

b.setSquare(7,0,6), b.setSquare(7,2,2), b.setSquare(7,3,3), b.setSquare(7,8,4)

b.setSquare(8,5,7), b.setSquare(8,6,9)
print(b)
print('wait a moment please\n')
print(solve(b))