def between(start, end):
	return list(map(int, range(start, end+1)))
def aNumber(nbr):
	return nbr.isdigit()
def getName():
	name = input('Enter a name: ')
	while not all(letter.isalpha() or letter.isspace() for letter in name):
		name = input(str(name) + " is not a name that only contains letters or spaces, re-enter: ")
	return name
def getAge():
	age = input('Enter your age: ')
	while not aNumber(age) or float(age) not in between(0,120): #if number between 0 and 120
		age = input(str(age) + " is not a number or reasonable age, re-enter: ")
	return float(age)
def findMax(array):
	maxNbr = max(array)
	for (index, nbr) in enumerate(array):
		if float(nbr) == maxNbr:
			return index
def maxAge(numberOfStudents):
	names = []
	ages = []
	for i in range(numberOfStudents):
		names.append(getName())
		ages.append(getAge())
	maxAge = findMax(ages)
	return [names[maxAge], ages[maxAge]]