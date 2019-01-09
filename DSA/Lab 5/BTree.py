class Node:
	def __init__(self,value=None,left=None,right=None):
		self.value=value
		self.left=left
		self.right=right
		self.parent=None


def pretrav(node):
	curr=node
	if(curr!=None):
		print(curr.value," ",end="")
		pretrav(curr.left)
		pretrav(curr.right)
	else:
		return





class BTree:
	def __init__(self,root=None):
		self.root=root

	def insert(self,value):
		curr=self.root
		x=Node(value)
		while(curr!=None):
			if curr.value>value:
				if curr.left==None:
					curr.left=x
					x.parent=curr
					return
				else:
					curr=curr.left

			else:
				if curr.right==None:
					curr.right=x
					x.parent=curr
					return
				else:
					curr=curr.right

				

		

	def search(self,value):
		curr=self.root
		while(curr!=None):
			if curr.value>value:
				curr=curr.left
			elif(curr.value<value):
				curr=curr.right
			else:
				return curr

		return None


	def delete(self,value):
		curr=self.search(value)
		if(curr.left==None and curr.right==None):
			if(curr.parent.left==curr):
				curr.parent.left=None
			else:
				curr.parent.right=None

		elif(curr.left==None and curr.right!=None):
			if(curr.parent.left==curr):
				curr.parent.left=curr.right
			else:
				curr.parent.right=curr.right

		elif(curr.left!=None and curr.right==None):
			if(curr.parent.left==curr):
				curr.parent.left=curr.left
			else:
				curr.parent.right=curr.left
		
		else:
			s=self.succ(curr.value)
			curr.value=s.value

			if(s.parent.left==s):
				s.parent.left=None
			else:
				s.parent.right=None









	def maxi(self,node):
		curr=node
		while(curr.right!=None):
			curr=curr.right
		return curr

	def mini(self,node):
		curr=node
		while(curr.left!=None):
			curr=curr.left
		return curr

	def pred(self,value):
		x=self.search(value)

		if(x.left!=None):
			return self.maxi(x.left)
		else:
			y=x.parent
			while(y!=None and x==y.left):
				x=y
				y=y.parent
			return y

	def succ(self,value):
		x=self.search(value)

		if(x.right!=None):
			return self.mini(x.right)
		else:
			y=x.parent
			while(y!=None and x==y.right):
				x=y
				y=y.parent
			return y






def main():
	root=Node(10)
	T=BTree(root)
	T.insert(5)
	T.insert(12)
	T.insert(8)
	T.insert(11)
	print("Maximum value =",T.maxi(T.root).value)
	print("Minimum value =",T.mini(T.root).value)
	if(T.search(6) == None):
		print("Not Found")
	else:
		print("Found")


	print("succ :",T.succ(8).value)
	print("pred:",T.pred(8).value)


	pretrav(T.root)
	print()
	T.delete(5)
	pretrav(T.root)
	print()




	

main()




		






