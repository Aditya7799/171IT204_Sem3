# class Stack:
# 	def __init__(self):
# 		self.l=[]

# 	def push(self,value):
# 		self.l.append(value)

# 	def pop(self):
# 		x=self.l.pop()
# 		return x

def pretrav(node):
	curr=node
	if(curr!=None):		
		print(curr.value," ",end="")
		pretrav(curr.left)
		pretrav(curr.right)
	else:
		return

def posttrav(node):
	curr=node
	if(curr!=None):		
		posttrav(curr.left)
		posttrav(curr.right)
		print(curr.value," ",end="")
	else:
		return










def eval(node):
        if(node.left==None and node.right==None):
                return int(node.value)
        else:
                if(node.value=='+'):
                   return eval(node.left)+eval(node.right)
                if(node.value=='-'):
                   return eval(node.left)-eval(node.right)
                if(node.value=='*'):
                   return eval(node.left)*eval(node.right)
                if(node.value=='/'):
                   return eval(node.left)/eval(node.right)
        
                
        


class Node:
	def __init__(self,value=None,left=None,right=None,parent=None):
		self.value=value
		self.right=right
		self.left=left
		self.parent=parent

class BTree:
	def __init__(self,root=None):
		self.root=root

	def parsetree(self,l):
		curr=self.root
		for i in range(0,len(l)):
			if(l[i]=='(' or l[i] == '['):
				temp=Node()
				curr.left=temp
				temp.parent=curr
				curr=curr.left
			elif(l[i]!='+' and l[i]!='-' and l[i]!='*' and l[i]!='/' and l[i]!=')' and l[i]!= ']'):
				curr.value=l[i]
				curr=curr.parent
			elif(l[i]=='+' or l[i]=='-' or l[i]=='*' or l[i]=='/'):
				if(curr.value==None):
					curr.value=l[i]
					temp=Node()
					curr.right=temp
					temp.parent=curr
					curr=curr.right
				else:
					temp=Node()
					temp.value=l[i]
					temp.left=curr
					curr.parent=temp								
					node=Node()
					curr=curr.parent
					curr.right=node
					node.parent=curr
					curr=curr.right
					self.root=temp


			elif(l[i]==']' or l[i] ==')'):
				curr=curr.parent

	







	






def main():
	root=Node()
	S=BTree(root)
	print("Enter the xpression")
	expr=input()
	l=[]


	for i in expr:
		l.append(i)

	S.parsetree(l)
	print("PreOrder Traversal:")
	pretrav(S.root)
	print()
	print("Post Order Traversal:")
	posttrav(S.root);
	print()
	print("Value:")
	print(eval(S.root))



	
main()





