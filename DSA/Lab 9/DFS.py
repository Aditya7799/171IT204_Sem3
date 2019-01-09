class Node:
	def __init__(self,value=None,next=None):
		self.value=value 
		self.next=next
		self.color="white"
		self.s_time=-1
		self.e_time=-1
		



time=-1
l=[]

class Graph:
	def __init__(self,nodes=None):
		self.nodes=nodes
		self.adlist=[None]*nodes
		
		

	def insert(self,a,b):
		temp=self.adlist[a]
		self.adlist[a]=Node(b,temp)

	def setColor(self,value,color):
		for i in self.adlist:
			curr=i
			while(curr!=None):
				if(curr.value==value):
					curr.color=color
				curr=curr.next

	def set_STime(self,value,s_time):
		for i in self.adlist:
			curr=i
			while(curr!=None):
				if(curr.value==value):
					curr.s_time=s_time
				curr=curr.next

	def set_ETime(self,value,e_time):
		for i in self.adlist:
			curr=i
			while(curr!=None):
				if(curr.value==value):
					curr.e_time=e_time
				curr=curr.next

	def DFS(self,v):
		global time
		global l
		self.setColor(v,"gray")
		l.append(v)
		print(v," ",end="")
		time=time+1
		self.set_STime(v,time)
		curr=self.adlist[v]
		while(curr!=None):
			if(curr.color=="white"):
				self.DFS(curr.value)
			curr=curr.next
		self.setColor(v,"black")
		time=time+1
		self.set_ETime(v,time)

	def printTStamps(self,value):
		for i in self.adlist:
			curr=i
			while(curr!=None):
				if(curr.value==value):
					print(str(curr.s_time)+" "+str(curr.e_time))
					return
				curr=curr.next







		






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
	global l
	g.DFS(0)
	print("Time stamps are as follows")
	# nodes=nodes-1
	# while(nodes>=0):
	# 	print("For node ",str(nodes),":",end="")
	# 	g.printTStamps(nodes)
	# 	nodes=nodes-1
	for i in l:
		print("For node ",i,":",end="")
		g.printTStamps(i)


main()

	
	







		
		
