# Write a method/function called hasConsecutiveValues that takes as input an array (or Python list) 
# that contains only integers. The function returns true if the array has any 2 values that are consecutive, 
# and returns false if it does not. 2 integer values are consecutive if there is no other integer in between them.
# 
# Example:
#     input: [3, 10, 123, 10]         output: false
#     input: [35, 12, 13]             output: true
#     input: [4, 3]                 output: true
#     input: [723, 5409, 12, 722, 45]     output: true
#     input: [723, 5409, 12, 725, 45]     output: false

def hasConsecutiveValues(array):
	"""
	Inputs: 
	array (type : list):	list which contains only integers

	Outputs:
	bool:	indicates if list contains two consecutive values
	"""

	if len(array) < 2:
		return False
	
	for i in range(len(array)):
		for j in range(i+1, len(array)):
			if abs(array[i] - array[j]) == 1:
				return True
	return False


if __name__ == "__main__":
	array = [1, 892, 739, 9173, 83, -98, 891]

	print(hasConsecutiveValues(array))
