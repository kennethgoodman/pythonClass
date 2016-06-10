#similar to class 2 between() but uses numbers instead
#check classFile for class 2 for explanation of function
def between(start, end):
	return list(map(int, range(start, end+1)))
#checks if input is number
def aNumber(nbr):
	return nbr.isdigit()
name = input('Enter a name: ')
#does the loop while not all of the characters in name are either
# an alphabetic character (isalpha()) or a space 
while not all(character.isalpha() or character.isspace() for character in name): 
	name = input(str(name) + " is not a name that only contains letters or spaces, re-enter: ")
print('Hello ' + name)

age = input('Enter your age: ')
while not aNumber(age) or float(age) not in between(0,120): #if number between 0 and 120
	age = input(str(age) + " is not a number or reasonable age, re-enter: ")
print(name + ",", 'you are', age,'years old')


# gets three names and prints them
kids = []
while len(kids) < 3:
	kid = input("enter a name: ")
	while not all(letter.isalpha() or letter.isspace() for letter in kid):
		kid = input(str(kid) + " is not a name that only contains letters or spaces, re-enter: ")
	kids.append(kid)
print(kids)