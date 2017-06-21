class Stack(object):
	
	#constructor for the stack
	#takes no arguements
	def __init__(self):
		self.container = []

	#returns true if empty and false otherwise
	def isEmpty(self):
		if len(self.container) == 0:
			return True
		else:
			return False
	
	#this method adds an element to the front of the stack
	def push(self, newItem):
		self.container.insert(0, newItem)

	#this method takes out the element in front of 
	#the stack and returns it
	#returns False if list is empty
	def pop(self):
		
		if self.isEmpty():
			return False

		itemToPop = self.container[0]
		del self.container[0]
		return itemToPop

	#returns the top element of the stack if there is 
	#something, else false otherwise
	def peek(self):
		if self.isEmpty():
			return False

		return self.container[0]

	#prints the contents of the stack
	def printStack(self):
		print(self.container)
