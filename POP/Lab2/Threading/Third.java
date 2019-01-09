import java.util.Scanner;
class Third{

	public static boolean isArmStrong(int a){
		int length = (Integer.toString(a)).length();
		int sum=0;

		while(a>0){
			int r = a%10;
			sum=sum+(int)Math.pow(r,length);
			a=a/10;
		}

		if(sum==a)
			return true;
		else
			return false;


	}


	public static void main(String args[]){
		Scanner s = new Scanner(System.in);
		int a =s.nextInt();

		if(isArmStrong(a))
		System.out.println("YEs");
	}
}