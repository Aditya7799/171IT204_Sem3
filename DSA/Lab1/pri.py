

n=input("enter number: ")
a="True"

if n<=1:
	a="False"

for i in range(2,n):
	if(n%i==0):
		a="False"
		break
	else:
		a="True"
		
print(a)