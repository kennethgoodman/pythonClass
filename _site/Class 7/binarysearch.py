def binarySearch(listOfNumbers,number,debug=False):
	if debug:
		print(listOfNumbers)
	length = len(listOfNumbers)

	if listOfNumbers[length//2] == number:
		return True
	if length == 1:
		return False
	elif listOfNumbers[length//2] > number:
		return binarySearch(listOfNumbers[:length//2], number,debug=debug)
	else: # if its less than number
		return binarySearch(listOfNumbers[length//2:], number,debug=debug)
#example:
a = range(1,25)
print(binarySearch(a,1,debug=True))