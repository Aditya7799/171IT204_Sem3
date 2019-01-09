class Fraction:

	def __init__(self,a,b):
		self.num=a
		self.den=b

	
	def gcd(self):
		a=self.num
		b=self.den
		gcd=1

		if(b>a):
			temp=a
			a=b
			b=temp
		
		for i in range(1,a):
			if(a%i==0 and b%i==0):
				gcd=i
		return gcd

		

	def inverse(self):
		a=Fraction(self.den,self.num)
        # fac=a.gcd()
        # a.num=int(a.num/fac)
        # a.den=int(a.den/fac)
        return a

		

		

	def add(self,f):
		a=Fraction(1,1)
		a.num=self.num*f.den + self.den*f.num
		a.den=self.den*f.den
		fac=a.gcd()

		a.num=int(a.num/fac)
		a.den=int(a.den/fac)
		return a


	def subtract(self,f):
		a=Fraction(1,1)
		a.num=self.num*f.den - self.den*f.num
		a.den=self.den*f.den
		fac=a.gcd()

		a.num=int(a.num/fac)
		a.den=int(a.den/fac)
		return a

		

	def multiply(self,f):
		a=Fraction(1,1)
		a.num=self.num*f.num
		a.den=self.den*f.den
		fac=a.gcd()

		a.num=int(a.num/fac)
		a.den=int(a.den/fac)
		return a

	def divide(self,f):
		a=Fraction(1,1)
		a.num=self.num*f.den
		a.den=self.den*f.num
		fac=a.gcd()

		a.num=int(a.num/fac)
		a.den=int(a.den/fac)
		return a

	


	def __str__ (self):
		return (str(self.num)+"/"+str(self.den))


	
def main():
	f1=Fraction(12,8)
	f2=Fraction(4,8)
	print(f1)
	
	print("THe sum is",f1.add(f2))
	print("THe subtraction gives",f1.subtract(f2))
	print("THe multiplication gives",f1.multiply(f2))
	print("THe division gives",f1.divide(f2))
	print("THe inverse of f1 gives",f1.inverse())
































main()





	
		
