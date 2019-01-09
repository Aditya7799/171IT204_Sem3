class Node:
	def __init__(self,value=None,left=None,right=None,parent=None,height=None):
		self.value=value
		self.left=left
		self.right=right
		self.parent=parent
		self.height=height


class AVLTree:
	def __init__(self,root=None):
		self.root=root

	def insert(self,val):
		curr=val.root
		while(curr!=None):
			
			if(curr.value<value):
				if(curr.right!=None):
					curr.height=curr.height+1
					curr=curr.right
				else:
					temp=Node()
					temp.value=val
					temp.parent=curr
					curr.right=temp
					temp.height=1
					if(curr.left==None):
						curr.height=curr.height+1
					break

			elif(curr.value>value):
				if(curr.left!=None):
					curr.height=curr.height+1
					curr=curr.left
				else:
					temp=Node()
					temp.value=val
					temp.parent=curr
					curr.left=temp
					temp.height=1
					if(curr.right==None):
						curr.height=curr.height+1
					break

		n=temp
		z=n.parent
		y=n
		x=n


		while(z!=None):
			if(checkimbalance(z.left,z.right)):
				break
			else:
				x=y
				y=z
				z=z.parent

		#case1
		if(z.left==y and y.left==x):
			z.left=y.right
			
			y.right=z
			if(z.parent.left==z):
				z.parent.left=y
			else:
				z.parent.right=y
		#case2
		if(z.right=y and y.right=x):
			z.right=y.left
			y.left=z
			if(z.parent.left==z):
				z.parent.left=y
			else:
				z.parent.right=y

		#case3
		if(z.left==y and y.right==x):
			y.right=x.left
			x.left=y









