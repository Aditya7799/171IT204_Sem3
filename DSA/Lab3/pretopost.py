from mystack import Stack

def conv(expr):
	S = Stack()
	l=expr.split()
	l.reverse()

	for i in l:
		if(i!='+' and i!= '-' and i!='/' and i!= '*'):
			S.push(i)
		else:
			a=S.pop()
			b=S.pop()
			S.push(str(a)+" "+str(b)+" "+str(i)+" ")

	print("The postfix expression is",str(S.pop()))










def main():
	expr = input('Enter the expression: ')
	conv(expr)
	
if __name__ == '__main__':
    main()



