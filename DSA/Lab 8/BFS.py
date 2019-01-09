class Node:
	def __init__(self,value=None,next=None):
		self.value=value 
		self.next=next
		self.dist=-1
		self.color="white"
		

class Queue:
	def __init__(self):
		self.l=[]
	def isEmpty(self):
		if(len(self.l)==0):
			return True
		else:
			return False
	def enq(self,value):
		self.l.append(value)

	def dq(self):
		a=self.l[0]
		del self.l[0]
		return a






class Graph:
	def __init__(self,nodes=None):
		self.nodes=nodes
		self.adlist=[None]*nodes
		
		

	def insert(self,a,b):
		temp=self.adlist[a]
		if(temp==None):
			self.adlist[a]=Node(b,None)
		else:
			self.adlist[a]=Node(b,temp)

	def setColor(self,value,color):
		for i in range(self.nodes):
			curr=self.adlist[i]
			while(curr!=None):
				if(curr.value==value):
					curr.color=color
				curr=curr.next

	

	def setDist(self,value,dist):
		for i in range(self.nodes):
			curr=self.adlist[i]
			while(curr!=None):
				if(curr.value==value):
					curr.dist=dist
				curr=curr.next

	def findDist(self,value):
		for i in range(self.nodes):
			curr=self.adlist[i]
			while(curr!=None):
				if(curr.value==value):
					return curr.dist
				curr=curr.next





	def BFS(self,value):
		#initializing everthing to default

		for i in range(self.nodes):
			curr=self.adlist[i]
			while(curr!=None):
					self.setDist(curr.value,-1)
					self.setColor(curr.value,"white")
				curr=curr.next









		self.setColor(value,"gray")
		self.setDist(value,0)
		print()
		q=Queue()
		q.enq(value)



		while(not(q.isEmpty())):
			x=q.dq()
			print(x,":Distance=",self.findDist(x))
			curr=self.adlist[x]
			while(curr!=None):
				if(curr.color=="white"):
					self.setColor(curr.value,"gray")
					self.setDist(curr.value,1+self.findDist(x))
					q.enq(curr.value)
				curr=curr.next
			self.setColor(x,"Black")




		print()


		
def main():
	nodes=int(input("Enter the number of nodes"))
	g=Graph(nodes)
	print("Enter the edges,-1 to break")
	while(True):
		a=int(input("Enter the source     "))
		b=int(input("Enter the destination"))
		if(a!=-1 and b !=-1 ):
			g.insert(a,b)
			g.insert(b,a)
		else:
			break

	g.BFS(0)
	




main()