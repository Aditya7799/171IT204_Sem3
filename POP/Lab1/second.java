import java.io.*;
import java.util.Scanner;


class second{


	public static void main(String args[]){

		Scanner s = new Scanner(System.in);
		System.out.println("Enter the two operands");
		int a = s.nextInt();
		int b = s.nextInt();
		s.nextLine();

		System.out.println("Enter the operator : +,-,*,/ :");
		char c = (s.nextLine()).charAt(0);


		switch(c){

			case('+'):
				System.out.println("The sum is "+(a+b));
				break;
			case('-'):
				System.out.println("the Difference is "+ (a-b));
				break;
			case('*'):
				System.out.println("The product is "+a*b);
				break;
			case('/'):
				try{System.out.println("The quotient is :"+a/b);}
				catch(Exception e)
				{
					System.out.println("Divide by zero not possible");
				}
				break;
			default:
				System.out.println("Invalid Operator");

		}

	}
}