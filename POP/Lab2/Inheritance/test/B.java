import java.io.*;



class B extends C{

	public int p;
	

	public void test()
	{

	System.out.println("p ="+p);
	
	}


	B(int a)
	{
		this.p=a+50;
		
		System.out.println("Inside Constructor B");
	}




	B()
	{
		p=35;
		
		System.out.println("Inside Constructor B");
	}


	










}