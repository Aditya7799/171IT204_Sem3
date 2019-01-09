interface fruit{

	void eatFruit();
	
}

interface vegetable{
	
	void eatVegtable();
}


class Orange implements fruit{

	public void eatFruit(){
		System.out.println("Eating Orange ");
	}


}


class Apple implements fruit{

	public void eatFruit(){
		System.out.println("Eating Apple");
	}

}


class Spinach implements vegetable
{
	public void eatVegtable(){
		System.out.println("Eating Spinnach");
	}

}

class Cabbage implements vegetable
{
	public void eatVegtable(){
		System.out.println("Eating Cabbage");
	}

}


abstract class AbstractFactory {
	abstract fruit getFruit(String Fru);
	abstract vegetable getVegetable(String Vege) ;
}




class fruitFactory extends AbstractFactory{

	fruit getFruit(String f){

		if(f.equalsIgnoreCase("orange")){

			return new Orange();
		}

		else if(f.equalsIgnoreCase("Apple")){

			return new Apple();
		}
		else
			return null;
	}

	vegetable getVegetable(String v){
		return null;
	}
}


class vegetableFactory extends AbstractFactory{

	fruit getFruit(String f){
		return null;
		
	}

	vegetable getVegetable(String v){
		if(v.equalsIgnoreCase("Spinach")){

			return new Spinach();
		}

		else if(v.equalsIgnoreCase("Cabbage")){

			return new Cabbage();
		}
		else
			return null;
	}
}



class Factory_Producer{

	static AbstractFactory getFactory(String fac){

		if(fac.equalsIgnoreCase("fruit")){
			return new fruitFactory();

		}

		else if (fac.equalsIgnoreCase("vegetable")){
			return new vegetableFactory();
		}
		else
			return null;
	}
}



public class Factory_Method{

	public static void main(String args[]){

		AbstractFactory f= Factory_Producer.getFactory("fruit");
		f.getFruit("orange").eatFruit();

	}
}




