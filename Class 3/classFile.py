def between(start, end):
	return list(map(int, range(start, end+1)))
def aNumber(nbr):
	return nbr.isdigit()
name = input('Enter a name: ')
while not all(letter.isalpha() or letter.isspace() for letter in name):
	name = input(str(name) + " is not a name that only contains letters or spaces, re-enter: ")
print('Hello ' + name)
age = input('Enter your age: ')
while not aNumber(age) or float(age) not in between(0,120): #if number between 0 and 120
	age = input(str(age) + " is not a number or reasonable age, re-enter: ")
print(name + ",", 'you are', age,'years old')

kidsInClass = 0
kids = []
while kidsInClass < 3:
	kid = input("enter a name: ")
	while not all(letter.isalpha() or letter.isspace() for letter in name):
		kid = input(str(name) + " is not a name that only contains letters or spaces, re-enter: ")
	kids.append(kid)
	kidsInClass = kidsInClass + 1
print(kids)