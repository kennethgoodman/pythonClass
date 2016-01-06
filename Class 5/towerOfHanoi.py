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
		print("")
def createTowers(number_of_rings):
	return [[i for i in range(number_of_rings,0,-1)],[],[]]
def move(towers, fromTower, toTower):
	if(len(towers[fromTower]) != 0 and (len(towers[toTower]) == 0 or towers[fromTower][-1] < towers[toTower][-1])):
		towers[toTower].append(towers[fromTower].pop())
	else:
		raise NameError("Illegal move")
def solve(height,towers, fromTower, toTower, withTower):
	if height >= 1:
		solve(height-1,towers, fromTower,withTower,toTower)
		move(towers,fromTower,toTower)
		solve(height-1,towers, withTower,toTower, fromTower)
def playTowersOfHanoi():
        print("playing")
	return
