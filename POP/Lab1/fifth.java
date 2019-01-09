import java.io.*;
import java.util.Scanner;

class fifth{


	public static void main(String args[]){
		Scanner s= new Scanner(System.in);

		System.out.println("Enter the sizeof teh array");
		int n = s.nextInt();

		int A[] = new int[n];

		System.out.println("Enter the elements of the array");
		for(int i =0;i<n;i++)
			A[i]=s.nextInt();
		// reversing the array

		System.out.println("The reversed Array is ");

			for(int i = 0;i<n;i++)
				System.out.println(A[n-i-1]);



	}
}