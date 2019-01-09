x=input("Enter the word")
i=0
while(i<len(x)):
	for j in range(97,123):
		a=x[0:i]+x[i+1:len(x)]
		print(a)
	i=i+1