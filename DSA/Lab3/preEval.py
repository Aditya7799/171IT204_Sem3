from mystack import Stack





def eval(a,i,b):
	if(i=='+'):
		return(int(a)+int(b))
	if(i=='-'):
		return(int(a)-int(b))
	if(i=='*'):
		return(int(a)*int(b))
	if(i=='/'):
		if(int(b)==0):
			return None
		return(int(a)/(int(b)*1.0))




def eval_prefix(expr):
	S=Stack()
	l=expr.split()
	l.reverse()

	for i in l:
		if(i!='+' and i!= '-' and i!='/' and i!= '*'):
			S.push(i)
		else:
			a=S.pop()
			b=S.pop()
			x=eval(a,i,b)
			if(x!=None):
				S.push(eval(a,i,b))
			else:
				print("Divide by Zero not possible")
				return


	print("Value :",str(S.pop()))




def main():
	expr = input('Enter the postfix expression: ')
	eval_prefix(expr)

if __name__ == '__main__':
    main()



