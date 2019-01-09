import java.util.Scanner;
import java.util.InputMismatchException;

class calc{

	public static void main(String args[])
	{
		double a,b,d;
		char c;

		Scanner s = new Scanner(System.in);
		try{


		System.out.println("Enter the first Operand");
		a=s.nextDouble();
		System.out.println("Enter the second Operand");
		b=s.nextDouble();
		s.nextLine();
		System.out.println("Enter +:Add \n -:Subtract \n *:Multiply \n /:Divide");
		c=(s.nextLine()).charAt(0);

		
		
			switch(c){

				case('+'):
					d=a+b;
					System.out.println("The sum is "+d);
					break;
				case('-'):
					d=a-b;
					System.out.println("The difference is"+d);
					break;
				case('*'):
					d=a*b;
					System.out.println("The product is"+d);
					break;
				case('/'):
					int f=(int)a/(int)b;
					System.out.print("The division gives"+f);
					



			}
		}

		catch(InputMismatchException e)
		{
			System.out.println("Invalid Input\nPlease Input Double values of Operand");
		}

		catch(ArithmeticException e){
	
			 System.out.println("Divide by zero not possible");
		}

		

		






		}


	















	}


