def between(start, end):
	return list(map(chr, range(ord(start.lower()),ord(end.lower())+1))) + list(map(chr, range(ord(start.upper()), ord(end.upper())+1)))
if 'c' in between('a','d'):
	print("c is in between")
if 'C' in between('a','d'):
	print("C is in between")
if 'f' not in between('a','d'):
	print("f is not in between")