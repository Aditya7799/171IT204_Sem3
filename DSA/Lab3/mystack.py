class Stack:
	def __init__(self):
		self.elements=[]
		self.top=-1

	def push(self,x):
		self.top=self.top+1
		self.elements.append(x)

	def pop(self):
		if (self.top==-1):
			print("Cannot Pop Stack is empty")
			return
		else:
			x=self.elements[self.top]
			self.elements=self.elements[0:self.top]
			self.top=self.top-1
			return x


	def isEmpty(self):
		if(self.top == -1):
			return True
		else:
			return False

	def __str__(self):
		return (str(self.elements))
