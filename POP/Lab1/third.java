import java.io.*;
import java.util.Scanner;

class third{

	public static void main(String args[]){



		Scanner s = new Scanner(System.in);
		System.out.println("Enter the size of the array");
		int n = s.nextInt();
		int A[] = new int[n];

		for(int i = 0 ;i<n;i++){

			System.out.println("Enter A["+i+"]");
			A[i]=s.nextInt();
			A[i]=A[i]%2;

		}

		for(int i = 0 ;i<n;i++){

			System.out.print("A["+i+"]="+A[i]);
			System.out.println();
			
		}






	}

}