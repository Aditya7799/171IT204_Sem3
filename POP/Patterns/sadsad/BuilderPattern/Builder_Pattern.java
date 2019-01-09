class Car{
	int Id;
	String Color;

	void setId(int id){
		this.Id=id;
	}

	void setColor(String Color){
		this.Color=Color;
	}


	void getId(){
		System.out.println("Id="+Id);
	}

	void getColor(){
		System.out.println("Color="+Color);
	}



}


class CarBuilder{
	Car o = new Car();

	CarBuilder setId(int id){
		o.setId(id);
		return this;
	}
	CarBuilder setColor(String color){
		o.setColor(color);
		return this;
	}
	CarBuilder getId(int id){
		o.getId();
		return this;
	}
	CarBuilder getColor(){
		o.getColor();
		return this;
	}

	Car build(){
		return o;
	}
}


public class Builder_Pattern{

	public static void main(String args[]){
		CarBuilder obj = new CarBuilder();
		Car c = obj.setId(10).setColor("Red").build();


	}
}