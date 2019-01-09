class Inst{
	String I_name;

	Inst(String name){
		I_name=name;
	}

	Inst(){
		I_name="NITK";
	}
}




class Dept extends Inst{

	String D_name;
	int TCred;

	Dept(String name,int a){
		D_name=name;
		TCred=a;


	}

	Dept(){
		D_name="IT";
		TCred=100;
	}

}


class Student extends Dept{
	String name;
	int Cred;

	Student(String name,int a )
	{	
		this.name=name;
		Cred=a;

	}

}
