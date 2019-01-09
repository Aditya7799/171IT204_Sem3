def gcd(a,b):
	max=a
	min=b
	if b>a:
		max=b
		min=a
	while min>0:
		min,max=max%min,min
	return max

n1=input("enter number1: ")
n2=input("enter number2: ")
print(gcd(int(n1),int(n2)))