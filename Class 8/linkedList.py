class LinkedList(object):
	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0
	def append(self,data):
		if self.size != 0:
			self.last.setNext(Node(data))
			self.last = self.last.getNext()
			self.size += 1
		else:
			self.first = self.last = Node(data)
			self.size = 1
	def prepend(self,data):
		if self.size != 0:
			node = Node(data)
			node.setNext(self.first)
			self.first = node
			self.size += 1
		else: #size is zero
			self.append(data)
	def search(self,data, ifFound):
		#check base case where size = 0
		current = last = self.first
		found = False
		while current and found is False:
			if current.getData() == data:
				found = True
				if ifFound:
					ifFound(last,current)
			else: #if less
				last = current
				current = current.getNext()
		if current is None:
			raise ValueError("Data not in list")
		return current
	def delete(self,data):
		# check base case where data is first
		search(data, lambda last, current: last.setNext(current.getNext()))
	def size(self):
		return self.size
	def __str__(self):
		current = self.first
		string = ""
		while current:
			string += str(current.getData()) + " -> "
			current = current.getNext()
		return string[:-4] # [:-4] b/c dont print last arrow
	def __len__(self): #for use with len(LinkedList)
		return self.size
	def __contains__(self, data): #for use with "x in LinkedList"
		try:
			self.search(data, None)
		except:
			return False #not found
		return True #Found
class Node():
	def __init__(self, data):
		self.data = data
		self.Next = None
	def setData(self,data):
		self.data = data
	def setNext(self,node):
		self.Next = node
	def getNext(self):
		return self.Next
	def getData(self):
		return self.data
#still testing
l = LinkedList()
for i in range(1,10):
	l.prepend(i)
print(l)