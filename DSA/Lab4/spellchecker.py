from linked_list import LinkedList,ListNode

class HashTable():

	def __init__(self):
		self.T=[None]*4999


	def hash_key(expr):
		i=0
		sum=0
		while(i<len(expr)):
			sum=sum*33+ord(expr[i])
			i=i+1
		return(sum % 4999)


	
	def insert(self,expr):
		key=HashTable.hash_key(expr)
		temp=ListNode()
		temp.value=expr
		temp.key=key
		temp.next=None

		if(self.T[key]==None):
			self.T[key]=temp

		elif(self.T[key]!= None):
			curr=self.T[key]
			self.T[key]=temp
			temp.next=curr


	def search(self,expr):	
		index = HashTable.hash_key(expr)
		if(self.T[index]==None):
			print("Does not exist in Has Table")
		else:
			curr=self.T[index]
			while(curr!=None):
				if(curr.value==str(expr)):
					print("Found in HashTable")
					return
				curr=curr.next

		print("Not Found in Hash Table")

	def __str__(self):
		s=""
		for i in self.T:
			if(i != None):
				s=s+"Key"+str(i.key)+":"
				curr=i
				while(curr!=None):
					s=s+curr.value+" "
					curr=curr.next
				s=s+"\n"
		return s

	def keys(self):
		l=[]
		for i in self.T:
			if(i!=None):
				l.append(i.key)
		return l








def main():
	H=HashTable()
	f=open("ispell.dict","r")
	s=f.read()
	s=s.split('\n')

	for i in s:
		H.insert(i)

	# # print(H)

	# # print(H.T[29].value)
	print(H)

	

	x=input("Enter the Word to be checked")
	print()
	H.search(x)



main()
