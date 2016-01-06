class Tree(object):
	"""docstring for tree"""
	def __init__(self, rootData):
		self.root = node(rootData)
		self.nodes = 0
	def append(self, data):
		return #implement
	def search(self, data):
		return
	def delete(self,data): #todo Implement
		return #not yet implemented
	def height(self):
		return self.root.calcHeight(self.root)
	def printLevelOrder(self,root):
		h = self.height()
		# implement
	def printGivenLevel(self,root, level, h,i):
		return #implement
class BinaryTree(Tree):
	def __init__(self,rootData):
		self.root = BinaryNode(rootData)
	def append(self,data):
		current = self.root
		last = current
		while current:
			last = current
			if(current.getData() > data):
				current = current.getNextLeft()
			else:
				current = current.getNextRight()
		if(last.getData() > data):
			last.setNextLeft(node(data=data))
		else:
			last.setNextRight(node(data=data))
		self.nodes += 1
	def search(self,data):
		current = self.root
		found = False
		while current and found is False:
			if(current.getData() == data):
				found = True
			elif current.getData() > data:
				current = current.getNextLeft()
			else: #if less
				current = current.getNextRight()
		if current is None:
			raise ValueError("Data not in list")
		return current
	def delete(self,data): #todo Implement
		return #not yet implemented
	def height(self):
		return self.root.calcHeight(self.root)
	def printLevelOrder(self,root):
		h = self.height()
		for i in range(1, h+1):
			print(" "*(2**(h-i+1)),end="") # 
			self.printGivenLevel(root, i, h,i)
			print("") #print new line
	def printGivenLevel(self,root, level, h,i):
		if root is None and level == 1:
			print(" " + " "*(2**(h-i + 2)-1),end="")
		elif root is None: #level does not equal 1
			for j in range(0, 2**(level-1)):
				print(" " + " "*(2**(h-i + 2)-1),end="")
		elif level == 1:
			print(str(root.getData()) + " "*(2**(h-i + 2)-1), end="")
		elif level > 1:
			self.printGivenLevel(root.getNextLeft(), level-1,h,i)
			self.printGivenLevel(root.getNextRight(), level-1,h,i)
	def __str__(self):
		self.printLevelOrder(self.root)
		return ""
class treeNode():
	def __init__(self, data=None):
		self.data = data
		self.nextNodes = []
	def getData(self):
		return self.data
	def setData(self, data):
		self.data = data
	def getNextNode(self, i):
		return self.nextNodes[i]
	def setNextNode(self, i, node):
		if(i > len(self.nextNodes)):
			raise
		self.nextNodes[i] = node
	def calcHeight(self, node):
		if node if None:
			return 0
		else:
			maxHeight = 0
			for i in nextNodes:
				maxHeight = max(maxHeight, node.calcHeight(node.getNextNode(i)))
			return maxHeight + 1
class BinaryNode(treeNode):
	def __init__(self,data=None):
		super().__init__(data)
	def getData(self):
		return self.data
	def setData(self, data):
		self.data = data
	def getNextLeft(self):
		return self.getNextNode(0)
	def getNextRight(self):
		return self.getNextNode(1)
	def setNextLeft(self, node):
		self.setNextNode(0, node)
	def setNextRight(self, node):
		self.setNextNode(1, node)
	def calcHeight(self,node):
		if node is None:
			return 0
		else:
			return max(node.calcHeight(node.getNextLeft()),node.calcHeight(node.getNextRight()))+1
	def createPrintString(self, level=0):
		ret = '\t'*level+repr(self.getData()) + "\n"
		if(self.getNextLeft()):
			ret += self.getNextLeft().createPrintString(level=level+1)
		if(self.getNextRight()):
			ret += self.getNextRight().createPrintString(level=level+1)
		return ret
	def __str__(self):
		return self.createPrintString()
#Still testing
n = 4
t = BinaryTree(2**(n-1))
t.append(2), t.append(6)
t.append(1), t.append(3), t.append(5), t.append(7)
t.append(0), t.append(1.5), t.append(2.5), t.append(3.5), t.append(4.5), t.append(8)
# for i in range(10,15):
# 	t.append(i)
print(t)
#t.root.traverse(t.size)
#print(t.root)