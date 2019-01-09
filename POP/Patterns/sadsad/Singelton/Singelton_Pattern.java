class Singleton{

	private static Singleton obj = null;

	private Singleton(){
	}


	public static Singleton getInstance(){
		if(obj== null){
			obj=new Singleton();
			return  obj;
		}
		else
			return obj;
	}
}



public class Singelton_Pattern{

	public static void main(String args[]){

		Singleton x = Singleton.getInstance();
		Singleton y = Singleton.getInstance();

		if (x==y)
		{
			System.out.println("== operator checks if the objects are equal");

		}

		else
			System.out.println("They are not equal");
	}
}