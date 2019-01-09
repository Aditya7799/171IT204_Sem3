import java.io.*;
import java.util.Scanner;

class first{



	public static void main(String args[])
	{	System.out.print("Enter the Character");
		Scanner s = new Scanner(System.in);
		String str = s.nextLine();
		str=str.toLowerCase();
		char c = str.charAt(0);
		switch(c)
		{

			case('a'):
			case('e'):
			case('i'):
			case('o'):
			case('u'):
			System.out.println("The Character is a Vowel");
			break;
			default:
			System.out.println("The Character is a Consonant");

		}

		
	}
}