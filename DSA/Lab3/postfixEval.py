from mystack import Stack

def eval_postfix(s):
	l = s.split()

	S=Stack()
	for i in l:
		if(i!='*' and i!='/' and i!='+' and i !='-'):
			S.push(int(i))
			
		else:
			b=int(S.pop())
			a=int(S.pop())
			
			if(i=='*'):
				S.push(a*b)
			if(i=='/'):
				S.push(a/b)
			if(i=='+'):
				S.push(a+b)
			if(i=='-'):
				S.push(a-b)

	return S.pop()

    
    
def main():
	expr = input('Enter the postfix expression: ')
	print('The value of the expression is',eval_postfix(expr))

if __name__ == '__main__':
    main()

