# Write a method/function called hasDuplicates that takes an array (or Python list) 
# as input and then returns true if the array has any duplicates, and returns false if it does not.

# Example:
#     input: [3, 10, 123, 10]     output: true
#     input: [35, 12, 6]          output: false
#     input: [3, 3]               output: true

def hasDuplicates(array):
	"""
	Inputs:
	array (type: list): list of elements
	
	Outputs:
	boolean: indicates if array contains duplicates
	"""

	newlist = []
	for i in array:
		if i not in newlist:
			newlist.append(i)
		else:
			return True

	return False

if __name__ == "__main__":

	array = [1,3,4,55,69,29,38,2,0]

	print(hasDuplicates(array))
