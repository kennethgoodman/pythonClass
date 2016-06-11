if hasattr(__builtins__, 'raw_input'): #input now works for both python2.7 and python3 
	input=raw_input					   #Much better than sys.stdin.readline()

def between(start, end):
	return list(map(int, range(start, end + 1))) #returns list of numbers between start and end
# will eventually combine this with other between() for characters for more English-like code 
def aNumber(value): 
	try:
		float(value)
		return True     # any float or int will return true as opposed to just ints
	except ValueError:
		return False

def getName():
	print('Enter a name: ')
	while True:
		student_name = input()
		if all(character.isalpha() or character.isspace() for character in student_name):
			return student_name
		print(student_name + " is not a name that only contains letters or spaces, re-enter: ")	
def getAge():
	print('Enter your age: ')
	while True:
		age = input()
		if aNumber(age) and int(float(age)) in between(0, 120): #if number not between 0 and 120
			return int(age)
		print(str(age) + " is not a number or reasonable age, re-enter: ")
def findMaxIndex(array):
	maxIndex = 0
	for i in range(len(array)):
		if aNumber(array[i]) and array[i] > maxIndex:
			maxIndex = i
	return maxIndex
#change function to accept any string for any property
def getStudents(numberOfStudents):
	names = []
	ages = []
	for i in range(numberOfStudents):
		names.append(getName())
		ages.append(getAge())
	return names, ages 

def maxProperty(names, property):
	maxIndex = findMaxIndex(property) #returns index of highest age 
	return [names[maxIndex], property[maxIndex]]
#example:
names, ages = getStudents(3)
print( maxProperty(names, ages) ) 
