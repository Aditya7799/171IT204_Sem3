import java.util.Scanner;



class First{



		public static void main(String args[]){

			Scanner s = new Scanner(System.in);
			System.out.println("Enter the String");
			String str = s.nextLine();
			str=str.toLowerCase();
			int A[] = new int[26];
			for(int i = 0;i<str.length();i++)
				A[(int)(str.charAt(i))-97]++;

			for(int i =0;i<26;i++)
			{
				if(A[i]>=2){
					int a=97+i;
					System.out.println((char)a+" occurs "+A[i]+" times");
				}
			}


}
}