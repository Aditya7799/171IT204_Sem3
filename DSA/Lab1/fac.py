def fact(n):
	if n==1 or n==0:
		return 1
	elif n<0:
		return -1
	return n*fact(n-1)


n=input("enter number: ")
print(fact(int(n)))