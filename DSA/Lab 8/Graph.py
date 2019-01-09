class Node:
	def __init__(self,value=None,next=None):
		self.value=value 
		self.next=next





class Graph:
	def __init__(self,nodes=None):
		self.nodes=nodes
		#initalizing both the representations of the Graph
		self.adlist=[None]*nodes
		self.admatrix=[[0]*nodes for i in range(nodes)]
		

	def insert(self,a,b):
		if(a==b):
			return
		self.admatrix[a][b]=1
		temp=self.adlist[a]
		if(temp==None):
			self.adlist[a]=Node(b,None)
		else:
			self.adlist[a]=Node(b,temp)
		
	def printGraph(self):
		for i in range(self.nodes):
			curr=self.adlist[i]
			print("Vertex",i,":",end="")
			while(curr!=None):
				print(curr.value," ",end="")
				curr=curr.next
			print()

		for i in range(self.nodes):
			print(self.admatrix[i],end="")
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

	g.printGraph()
	




main()