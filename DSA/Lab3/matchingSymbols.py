from mystack import Stack

def isMatched(expr):
	S=Stack()
	for i in expr:
		if(i=='{' or i == '[' or i == '('):
			S.push(i)
			# print(i,"was pushed")
		elif(i=='}' or i == ']' or i == ')'):
			x=S.pop()
			# print(x,"was Popped for", i)
			if(not(equals(x,i))):
				return False


				
				

	if(S.isEmpty()):
		return True
	else:
		return False
    




def equals(x,i):
	if(x=='{' and i=='}'):
		return True
	if(x=='[' and i==']'):
		return True
	if(x=='(' and i==')'):
		return True
	
	return False







    
def main():
	expr = input('Enter the expression: ')
	if isMatched(expr):
		print('Matched symbols')
	else:
		print('Unmatched symbols')

if __name__ == '__main__':
    main()

