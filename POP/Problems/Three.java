
import java.util.Scanner;




class Three{

	public static void main(String args[])throws Exception
	{
		Prime obj1=new Prime(1000,2000);
		
		Prime obj2=new Prime(2000,3000);
		
		Prime obj3=new Prime(3000,4000);
		
		Prime obj4=new Prime(4000,5000);
		

		Scanner s = new Scanner(System.in);
		System.out.println("Enter A for Ascending or D for Descending");
		char choice=(s.nextLine()).charAt(0);
		if(choice=='A'){
			obj1.start();
			obj1.join();
			obj2.start();
			obj2.join();
			obj3.start();
			obj3.join();
			obj4.start();


		}
		else if(choice == 'B'){
			obj4.start();
			obj4.join();
			obj3.start();
			obj3.join();
			obj2.start();
			obj2.join();
			obj1.start();

		}

		



	}


}



class Prime extends Thread{
	int a,b;

	Prime(int a,int b)
	{
		this.a=a;
		this.b=b;

	}

	public void run(){
		System.out.println("Inside Thread");

		for(int i=a;i<=b;i++){
			int flag =0;
			for(int j =2;j<i;j++)
			{
				if(i%j==0)
					{flag=1;
					break;}
			}

			if(flag==0)
				System.out.println(i+" is Prime");


		}


	}
}