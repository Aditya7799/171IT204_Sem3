from linked_list import LinkedList,ListNode

class HashTable():

	def __init__(self):
		self.T=[None]*30


	def hash_key(expr):
		i=0
		sum=0
		while(i<len(expr)):
			sum=sum*33+ord(expr[i])
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
			return False
		else:
			curr=self.T[index]
			while(curr!=None):
				if(curr.value==expr):
					return True
				curr=curr.next

		return False


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
	l=[]
	valid_del=[]
	valid_ins=[]

	#print(H)

	

	x=input("Enter the word")
	i=0
	while(i<len(x)):
		for j in range(97,123):
			a=x[0:i]+chr(j)+x[i+1:len(x)]
			if(H.search(a)):
				l.append(a)
		i=i+1

	print(l)

	print("Valid words obtained by deleting a charcter:")
	i=0

	while(i<len(x)):
		a=x[0:i]+x[i+1:len(x)]
		if(H.search(a)):
			valid_del.append(a)
		i=i+1
	print(valid_del)

	print("Valid words obtained by inserting a charcter:")
	i=0

	while(i<len(x)):
		for j in range(97,123):
			a=x[0:i]+chr(j)+x[i:len(x)]
			if(H.search(a)):
				valid_ins.append(a)
		i=i+1
	print(valid_ins)




	


main()
