#prints the tower for towers of Hanoi. 
def printTowers(towers):
	maxLength = max(len(towers[0]),len(towers[1]),len(towers[2]))
	for i in range(maxLength-1,-1,-1):
		for j in range(0,3):
			if(i == 0 and len(towers[j]) == 0):
				print("_",end="  ")
			else:
				try: 
					print(str(towers[j][i]), end="  ")
				except:
					print("   ", end="")
		print("") #print new line
#create three lists, the first with n rings and the other two, empty
def createTowers(number_of_rings):
	return [[i for i in range(number_of_rings,0,-1)],[],[]]
# move the top ring:
# if the tower isn't empty and, 
#         the tower we are moving to is empty or it's top 
#         ring is larger than the tower we are moving from:
#              move the ring
# else the legality check failed and we throw an error
def move(towers, fromTower, toTower):
	if(len(towers[fromTower]) != 0 and (len(towers[toTower]) == 0 or towers[fromTower][-1] < towers[toTower][-1])):
		towers[toTower].append(towers[fromTower].pop())
	else:
		raise NameError("Illegal move")
# solve the problem recursively, move the top n-1 rings from
# the starting tower to the temp tower,
# then move n-1 rings from that tower to correct tower
def solve(height,towers, fromTower, toTower, withTower):
	if height >= 1:
		solve(height-1,towers, fromTower, withTower, toTower)
		move(towers,fromTower,toTower)
		solve(height-1, towers, withTower, toTower, fromTower)
def win(towers):
	if len(towers[0]) == 0 and (len(towers[1]) == 0 or len(towers[2]) == 0):
		return True
	return False
# need to implement 
def playTowersOfHanoi():
    rings = int(input("How many rings? "))
    towers = createTowers(rings)
    while True:
    	printTowers(towers)
    	fromTower = int(input("Which tower do you want to move from, 1, 2, or 3: "))-1 
    	toTower   = int(input("Which tower do you want to move to,   1, 2, or 3: "))-1
    	if(fromTower != toTower):
    		try:
    			move(towers,fromTower, toTower)
    		except NameError as error:
    			print(error)
    	if win(towers):
    		print("You Won")
    		return

playTowersOfHanoi()
