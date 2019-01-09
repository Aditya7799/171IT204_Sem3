from imp import *
#from minh import *

def Di(T,n,S):
	#T[S].dist=0
	for i in range(n):
		T[i].dist=10000
	T[S].dist=0
	H=Heap(n);
	for i in range(n):
		H.inserth(T[i])
	#H.print()
	while not H.isEmpty():
		w=H.extractmin()
		#H.print()
		temp=w.next
		while temp!=None:
			if T[temp.value].dist>w.dist+temp.dist:
				T[temp.value].dist=w.dist+temp.dist
				temp.dist=T[temp.value].dist

				H.updatePriority(temp,T[temp.value].dist)
				#H.print()
				T[temp.value].prev=w
			#print(temp.value,"::",T[temp.value].dist)
			#print(w.value,":::::",temp.value,"::",temp.dist)
			#print(w.value,":::::",temp.value,"::",T[temp.value].dist)
			temp=temp.next
	print()
	#for i in range(n):
	#	if T[i].dist!=10000:
	#		print(T[i].value,":::",T[i].dist)
	#	else:
	#		print(T[i].value,"::: Infinity")


def main():
	t=int(input("1,2"))
	n=int(input("Vertices:"))
	T=[None for i in range(n)]
	print()

	m=int(input("Edges:"))
	print("Source,Destination")
	for i in range(m):
		l=input()
		l.split()
		x=int(l[0])
		y=int(l[2])
		z=int(input("Distance:"))
		insert(T,x,y,z)
		if t==2:
			insert(T,y,x,z)
	ke(T,n)
	for i in range(n):
		if T[i]==None:
			T[i]=ListNode()
			T[i].value=i

	s=int(input("Give Source Vertex:"))
	Di(T,n,s)
	l=[]
	for v in range(n):
		
		if v!=s:
			temp=T[v]
			print("Path for Vertex",T[v].value,":",end=' ')
			if temp.prev==None:
				print("There is NO PATH      Distance=Infinity")
			else:
				while temp!=None:
					l.append(temp.value)
					#print(temp.value,end=' ')
					temp=temp.prev
				#print()
				for i in range(len(l)-1,-1,-1):
					print(l[i],end=' ')
				print( "   Distance=",T[v].dist)
				l.clear()
	print()

main()
