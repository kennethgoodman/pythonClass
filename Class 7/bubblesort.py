def bubblesort(array, debug = False):
	#ex: 
	# input:[3,6,1,5]
	# 1 - [3,6,1,5] - > [3,1,6,5] - > [3,1,5,6]
	# 2 - [3,1,5,6] - > [1,3,5,6]
	stillSwapping = True
	while stillSwapping:
		stillSwapping = False #assume we should stop
		for i in range(1, len(array)):
			if debug:
				print("New loop: " + str(array))
			if array[i-1] > array[i]:
				array[i-1], array[i] = array[i], array[i-1] #swap
				if debug:
					print("Swapping: " + str(array))
				stillSwapping = True #dont stop since we swapped
	return array
def bubblesortOptimized1(array, debug = False):
	stillSwapping = True
	length = len(array)
	while stillSwapping:
		stillSwapping = False #assume we should stop
		for i in range(1, length):
			if debug:
				print("New loop: " + str(array))
			if array[i-1] > array[i]:
				array[i-1], array[i] = array[i], array[i-1] #swap
				if debug:
					print("Swapping: " + str(array))
				stillSwapping = True #dont stop since we swapped
		length = length - 1
	return array
def bubblesortOptimized2(array,debug=False):
	length = len(array)
	while length != 0:
		newLength = 0 # assume we dont make any more swaps
		for i in range(1, length):
			if debug:
				print("New loop: " + str(array))
			if array[i-1] > array[i]:
				array[i-1], array[i] = array[i], array[i-1] #swap
				if debug:
					print("Swapping: " + str(array))
				newLength = i #change assumptions, to dont make any more past this
		length = newLength #dont need to check past the last swap
	return array

# Examples
array = [3,6,1,5]
bubblesort(array,debug=True)
print("done with bubblesort")
array = [3,6,1,5]
bubblesortOptimized1(array, debug=True)
print("done with bubblesortOptimized1")
array = [3,6,1,5]
bubblesortOptimized2(array, debug=True)
print("done with bubblesortOptimized2")