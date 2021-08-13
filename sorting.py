from math import ceil

################## BUBBLE SORT ##################
def bubble_sort(array):
	"""
	Inputs:
	array (type : list):	list of numbers

	Outputs:
	array (type : list): 	list of numbers sorted in ascending order
	"""

	tmpArray = array.copy()
	print(array)

	for n in range(len(array)):
		for i in range(len(array)-1):
			if array[i] > array[i+1]:
				temp = array[i+1]
				array[i+1] = array[i]
				array[i] = temp
			print("Iteration {0}.{1}: {2}".format(n+1, i+1, array))
		if tmpArray == array:
			break

	return array

################## SELECTION SORT ##################
def selection_sort(array):
	"""
	Inputs:
	array (type : list):	list of numbers

	Outputs:
	array (type : list): 	list of numbers sorted in ascending order
	"""

	print(array)

	for n in range(len(array)):
		# Switching minimum value in subarray with current array element
		minIndex = array.index(min(array[n:len(array)]))
		tmp = array[minIndex]
		array[minIndex] = array[n]
		array[n] = tmp

		print("Iteration {0}: {1}".format(n+1, array))
	
	return array

################## MERGE SORT ##################
def merge_sort(array):
	"""
	Inputs:
	array (type : list):	list of numbers

	Outputs:
	sortedArray (type : list): 	list of numbers sorted in ascending order
	"""

	print(array)
	
	if len(array) == 1:
		return array 
	else:
		left = merge_sort(array[0 : (len(array)+1)//2])
		right = merge_sort(array[(len(array)+1)//2 : len(array)])

		sortedArray = merge(left, right)

	print("Final sorted array: {0}".format(sortedArray))
	return sortedArray

def merge(left, right):
	"""
	Inputs:
	left (type : list):		list of numbers
	right (type : list):	list of numbers

	Outputs:
	array (type : list): 	conjoined list of numbers sorted in ascending order
	"""

	array = []
	print("Left: {0}\tRight: {1}".format(left, right))

	if len(left) == 1 and len(right) == 1:
		if left[0] <= right[0]:
			array.extend([left[0], right[0]])
		else:
			array.extend([right[0], left[0]])
		del right[0], left[0]

		print("Merged array: {0}".format(array))
		return array
	elif not left:
		return right
	elif not right:
		return left
	else:
		if left[0] <= right[0]:
			array.append(left[0])
			del left[0]
		else:
			array.append(right[0])
			del right[0]
		
		print("Merged array: {0}".format(array))
		array.extend(merge(left, right))

	print("Merged array: {0}".format(array))
	return array

################## QUICK SORT ##################
def quick_sort(array, pivot=False):
	"""
	Inputs:
	array (type : list):	list of numbers
	pivot (type : int):		array index about whose value in the array to partition 

	Outputs:
	sortedArray (type : list): 	list of numbers sorted in ascending order
	"""

	print(array)

	if len(array) == 1:
		return array 
	elif len(array) == 2:
		if array[0] > array[1]:
			print("Final sorted array: {0}".format([array[1], array[0]]))
			return [array[1], array[0]]
		print("Final sorted array: {0}".format([array[1], array[0]]))
		return array

	if not pivot:
		pivot = len(array)//2

	tmp = array[0]
	pivotElement = array[pivot]
	array[0] = pivotElement
	array[pivot] = tmp

	low = 1
	high = len(array) - 1

	print(array)
	print("Low: {1}, High: {0}\n".format(array[high], array[low]))

	while low <= high and low < len(array) and high > 0:
		if array[low] > pivotElement and array[high] < pivotElement:
			print("Low: {1}, High: {0} => Swap\n".format(array[high], array[low]))
			tmp = array[low]
			array[low] = array[high]
			array[high] = tmp

		if array[low] <= pivotElement:
			low += 1

		if array[high] >= pivotElement:
			high -= 1

		print(array)
		try:
			print("Low: {1}, High: {0}\n".format(array[high], array[low]))
		except IndexError:
			print("Low: {1}, High: {0}\n".format(array[high], "Out of range"))

	array[0] = array[high]
	array[high] = pivotElement
	print(array)

	if high == 0:
		high = 1

	left = quick_sort(array[0 : high])
	right = quick_sort(array[high : len(array)])

	sortedArray = left + right
	print("Final sorted array: {0}".format(sortedArray))

	return sortedArray

################## HEAP SORT ##################
def heap_height(array):
	"""
	Inputs:
	array (type : list):	list of numbers

	Outputs:
	height (type : int): 	height of heap
	"""
	count = self.size
	height = 0

	while count >= 0:
		count -= 2**height 
		height += 1

	return height

def percolate(array, j):
	"""
	Inputs:
	array (type : list):	list of numbers
	j (type : int):			index of element to be percolated in heap

	Outputs:
	array (type : list): 	list of numbers with percolated element
	"""

	while 2*j+1 < len(array):
		print("\tIndex " + str(j))
		# Internal nodes will have left child
		leftDiff = array[j] - array[2*j+1]
		try:
			rightDiff = array[j] - array[2*j+2]
		except IndexError:
			rightDiff = None

		if (rightDiff is None or leftDiff >= rightDiff) and leftDiff > 0:
			tmp = array[2*j+1] 
			array[2*j+1] = array[j]
			array[j] = tmp 
			j = 2*j + 1
		elif not rightDiff:
			break
		elif rightDiff > 0 and rightDiff > leftDiff:
			tmp = array[2*j+2] 
			array[2*j+2] = array[j]
			array[j] = tmp
			j = 2*j + 2
		else:
			break
		print(array)
	return array

def remove_root(array):
	"""
	Inputs:
	array (type : list):		list of numbers

	Outputs:
	array (type : list): 		list of numbers with root removed and replaced by last element
	root (type : <number>):		number at initial root
	"""
	root = array[0]
	array[0] = array[-1]
	del array[-1]
	return array, root

def heap_sort(array):
	"""
	Inputs:
	array (type : list):	list of numbers

	Outputs:
	sortedArray (type : list): 	list of numbers sorted in ascending order
	"""

	if len(array) == 1:
		return array 
	
	sortedArray = []
	for i in range(len(array)-1, -1, -1):
		# Conditions for internal nodes
		if i != 0 and 2*i + 1 < len(array):
			j = i
			print("\nPercolating Element at Index {0}...".format(i))
			array = percolate(array, j)

	while array:
		print("\nPercolating Element at Root...")
		array = percolate(array, 0)
		array, root = remove_root(array)
		print("New array: {0}".format(array))
		sortedArray.append(root)

	print("Final sorted array: {0}".format(sortedArray))
	return sortedArray	


if __name__ == "__main__":
	# array = [6.67, 3, 43.5, -77.7, -0.8, 5.4, 5.55, 121.9, 7, 1, 0, 3]
	# array = list(range(11,-3,-1))
	# array = [2, 1, 4, 3, 5]
	# array = list(range(-5,19))
	array = [0,1,2,6,4,5]

	# bubble_sort(array)
	# selection_sort(array)
	# merge_sort(array)
	# quick_sort(array)
	heap_sort(array)
	