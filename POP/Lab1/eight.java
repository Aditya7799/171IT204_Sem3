import java.io.*;
import java.util.Scanner;

class eight{


	public static void main(String args[]){

		Scanner s = new Scanner(System.in);
		System.out.println("Enter the String");
		String str = s.nextLine();
		int count = 0;
		int word_count = 1;
		for(int i=0;i<str.length();i++)
		{	
			if(str.charAt(i)==' ')
			{
				System.out.println("Word "+word_count+" has "+count+" letters");
				count = 0;
				word_count++;
			}

			else
			{
				count++;
			}			}

		}
		
	}
