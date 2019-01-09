
import java.io.*;


class A extends B implements I{
	public int x;
	

	public static void main(String args[]){

		// B obj = new A();
		// System.out.println("p ="+obj.p);
		




		A obj2 = new A(23);
		System.out.println("p ="+obj2.p);
		System.out.println("x ="+obj2.x);
		System.out.println("c ="+obj2.c);
		
		


		// C obj3 = new A();
		// System.out.println("c="+obj3.c);








		





	}

	A()
	{
		x=44;
		System.out.println("Inside Constructor A");
		
	}



	A(int a)
	{	
		//super(a);
		this.x = a;
		
		System.out.println("Inside Contructor A");
	}


	public void abc(){
		System.out.println("Inside abc");
	}

	public void  bcd(){
		System.out.println("Inside bcd");
	}









}


			






