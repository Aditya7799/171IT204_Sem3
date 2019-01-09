

n=input("enter size of list: ")
a=[]
for i in range(int(n)):
	a.append(int(input()))

print (a)

for i in range(len(a)-1):
		for j in range((len(a)-1)):
			if(a[j]>a[j+1]):
				t=a[j]
				a[j]=a[j+1]
				a[j+1]=t









print(a)