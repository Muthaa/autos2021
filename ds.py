def array():
	nlist=[1,3,7,4]
	if 3 in nlist:print(True)
	for n in nlist:
		if n==1:
			print (True)

class node:
	"""object for node for storing a single node of a linked list of data and next node in list"""
	data = None
	next_node = None

	def __init__(self, data):
		super(node, self).__init__()
		self.data = data
		
	def __repr__(self):
		return "<Node data: %s>" %self.data

class linkedlst:
	'''Singly linked list'''
	def __init__(self):
		self.head = None

	def is_empty(self):
		return self.head == None
		
	def size(self):
		current = self.head
		count = 0

		while current:
			count +1
			current = current.next_node

			return count
if __name__ == '__main__':
	array()
	