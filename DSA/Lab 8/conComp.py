class Node:
	def __init__(self,value=None,next=None):
		self.value=value 
		self.next=next
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

	

	def conComp(self):
		#initializing everthing to default

		for i in range(self.nodes):
			curr=self.adlist[i]
			while(curr!=None):
				self.setColor(curr.value,"white")
				curr=curr.next
		z=1
		l=[-1]*self.nodes
		v=0




		while (v<self.nodes):
			self.setColor(v,"gray")
			
			
			q=Queue()
			q.enq(v)

			while(not(q.isEmpty())):
				x=q.dq()
				
				l[x]=z
				curr=self.adlist[x]
				while(curr!=None):
					if(curr.color=="white"):
						self.setColor(curr.value,"gray")
						q.enq(curr.value)
					curr=curr.next
				self.setColor(x,"Black")
			z=z+1
			try:
				v=l.index(-1)
			except ValueError:
				v=self.nodes+1
		z=z-1

		
		print()
		while(z>0):
			print("Component ",z,":",end="")
			i=0
			while(i<self.nodes):
				if(l[i]==z):
					print(i," ",end="")
				i=i+1
			z=z-1
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

	g.conComp()

	




main()