class Shape{
	int a;
	int b;

	Shape(int a){
	this.a =a;
	}

	Shape(int a,int b){
		this.a=a;
		this.b=b;
		}

	void area(int a){
		System.out.print("Area is "+3.14*a*a);
	}

	void area(int a, int b){
		System.out.print("Area is "+a*b);

	}



	public static void main(String args[]){
		Shape a = new Shape(3);
		Shape x = new Shape(2,6);
		a.area(4);a.area(4,6;)
	}
}