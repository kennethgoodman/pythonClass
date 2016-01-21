#uses ord() to convert the two characters to their corresponding ascii values, 
# then get that range of numbers. 
#Having the range of numbers (that represent the characters in ascii) it will map those numbers 
# back their corresponding character values and put it in a list. 
# the first list is lower case. The second is uppercase. 
# this function currently does no testing against incorrect input(such as numbers, two or more letter strings, backwards ranges (d->a), etc. 
def between(start, end): 
	return list(map(chr, range(ord(start.lower()),ord(end.lower())+1))) + list(map(chr, range(ord(start.upper()), ord(end.upper())+1)))
# examples:
if 'c' in between('a','d'): #show that it works with lowercase
	print("c is in between")
if 'C' in between('a','d'): #works with uppercase
	print("C is in between")
if 'f' not in between('a','d'): #show that will sometimes come up false
	print("f is not in between")