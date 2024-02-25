def linear_search(list,target):
	"""
	Return the index position in a list else return none"""
	for i in range (0, len(list)):
		if list[i] == target:
			return i
	return None

el=[1,3,4]
result = linear_search(el, 6)

def binary_search(list, target):
	first = 0
	last = len(list)-1

	while first<=last:
		midpoint = (first+last) //2

		if list[midpoint] == target:
			return midpoint
		elif list[midpoint] < target:
			return midpoint + 1
		else:
			return midpoint -1
			
	return None

def recursive_binary_search(list, target):
	if len(list) == 0:
		return False
	else:
		midpoint = len(list) // 2
		if list[midpoint] == target:
			return True
		if list[midpoint] < target:
			return recursive_binary_search(list[midpoint+1:],target)
		else:
			return recursive_binary_search(list[:midpoint], target)