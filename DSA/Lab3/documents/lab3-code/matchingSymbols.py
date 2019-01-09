from mystack import Stack

def isMatched(expr):
    """Checks if the expression 'expr' has matching opening/closing symbols."""
    pass
    
def main():
	expr = input('Enter the expression: ')
	if isMatched(expr):
		print('Matched symbols')
	else:
		print('Unmatched symbols')

if __name__ == '__main__':
    main()

