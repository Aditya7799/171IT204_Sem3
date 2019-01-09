import java.io.*;
import java.util.Scanner;


class ninth{


	public static void main(String args[]){

		Scanner s = new Scanner(System.in);
		System.out.println("Enter the String");
		String str = s.nextLine();

		String s2="";

		for( int i = 0 ; i < str.length();i++)
			s2+=str.charAt(i);


		System.out.println(s2);

	}
}