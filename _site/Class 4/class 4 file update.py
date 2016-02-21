import sys #for readline
#python 2 needs raw_input()
#python 3 needs input()
def between(start, end):
	return list(map(int, range(start, end+1))) #returns list of numbers between start and end
# will eventually combine this with other between() for characters for more English-like code 
def aNumber(nbr):
	return nbr.isdigit()
def getName():
	print('Enter a name: ')
	student_name = sys.stdin.readline()
	while not all(character.isalpha() or character.isspace() for character in student_name):
		print(str(student_name) + " is not a name that only contains letters or spaces, re-enter: ")
		student_name = sys.stdin.readline()
	return student_name
def getAge():
	print('Enter your age: ')
	age = sys.stdin.readline()
	while not aNumber(age) or float(age) not in between(0,120): #if number not between 0 and 120
		print(str(age) + " is not a number or reasonable age, re-enter: ")
		age = sys.stdin.readline()
	return float(age)
def findMax(array):
	maxNbr = max(array)
	for (index, nbr) in enumerate(array):
		if float(nbr) == maxNbr:
			return index
#change function to accept any string for any property
def getStudents(numberOfStudents):
       #maybe change to list of tuples instead of two lists
	names = []
	ages = []
	for i in range(numberOfStudents):
		names.append(getName())
		ages.append(getAge())
	return names,ages 
def maxProperty(names, property):
	indexOfMaxProperty = findMax(property) #returns index of highest age 
	return [names[indexOfMaxProperty], property[indexOfMaxProperty]]
#example:
names, ages = getStudents(3)
print( maxProperty(names, ages) ) 
