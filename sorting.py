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


if __name__ == "__main__":
	array = [6.67, 3, 43.5, -77.7, -0.8, 5.4, 5.55, 121.9, 7]
	# array = list(range(11,-3,-1))
	# array = [2, 1, 4, 3, 5]

	# bubble_sort(array)
	# selection_sort(array)
	# merge_sort(array)
	
