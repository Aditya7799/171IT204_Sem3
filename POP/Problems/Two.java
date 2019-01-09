


class Singleton{
	public static Singleton obj =null;

	private Singleton(){}

	public static synchronized Singleton getInstance(){
		if(obj == null)
			obj=new Singleton();
			
		return obj;


	}


}



class Multi_Thread1 extends Thread{



	public void run(){
		Singleton obj = Singleton.getInstance();
		System.out.println("The hascode of the Created Singleton object in Multi_Thread1 is "+obj.hashCode());
	}
}


class Multi_Thread2 extends Thread{



	public void run(){
		Singleton obj = Singleton.getInstance();
		System.out.println("The hascode of the Created Singleton object in Multi_Thread2 is "+obj.hashCode());
	}
}



public class Two{


	public static void main(String args[])throws Exception{

		Multi_Thread1 obj1=new Multi_Thread1();
		Multi_Thread2 obj2= new Multi_Thread2();

		obj1.start();
		obj1.sleep(0,800);
		obj2.start();

	}
}