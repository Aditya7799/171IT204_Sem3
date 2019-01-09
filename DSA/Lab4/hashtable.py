from linked_list import LinkedList,ListNode



# def hash_key(expr):
# 		i=0
# 		sum=0
# 		while(i<len(expr)):
# 			sum=sum+ord(expr[i])
# 			i=i+1
# 		return(sum % 30)



class HashTable():

	def __init__(self):
		self.T=[None]*30


	def hash_key(expr):
		i=0
		sum=0
		while(i<len(expr)):
			sum=sum+ord(expr[i])
			i=i+1
		return(sum % 30)



	
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
				if(curr.value==expr):
					print("Found in HashTable at key:",str(index))
					return
				curr=curr.next

		print("Not Found in Has Table")


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
	H=HashTable();
	
	H.insert("cat")
	H.insert("dog")
	H.insert("rat")
	H.insert("mice")
	H.insert("lion")
	H.insert("sad")
	H.insert("fox")
	H.insert("cow")
	H.insert("cock")
	H.insert("tom")
	H.insert("Jerry")
	print(H)
	print(H.keys())
	H.search("dog")

main()


	







