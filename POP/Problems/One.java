import java.awt.*;
import javax.swing.*;



interface Shape{
	public void draw();
}


class Circle extends JPanel implements Shape
{
	public void draw(){
		JFrame frame=new JFrame();
		frame.getContentPane().add(new Circle());
		frame.setSize(200,200);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);

	}


	public void paint(Graphics g){
		
		g.drawArc(50,50,100,100,0,360);			
	}
}


class Square extends JPanel implements Shape
{
	public void draw(){
		JFrame frame=new JFrame();
		frame.getContentPane().add(new Square());
		frame.setSize(200,200);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);

	}


	public void paint(Graphics g){
		
		g.drawRect(50,50,100,100);		
	}
}


class Rectangle extends JPanel implements Shape
{
	public void draw(){
		JFrame frame=new JFrame();
		frame.getContentPane().add(new Rectangle());
		frame.setSize(200,200);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);

	}


	public void paint(Graphics g){
		
		g.drawRect(50,50,100,50);			
	}
}



class ShapeFactory{

	public Shape getShape(String str){
		if(str.equalsIgnoreCase("Circle"))
			return new Circle();
		else if(str.equalsIgnoreCase("Square"))
			return new Square();
		else if (str.equalsIgnoreCase("Rectangle"))
			return new Rectangle();
		else 
			return null;

	}
}











public class One{

	public static void main(String args[]){
		
		ShapeFactory factory=new ShapeFactory();

		Shape s=factory.getShape("circle");
		s.draw();

		s=factory.getShape("square");
		s.draw();
		

		s=factory.getShape("rectangle");
		s.draw();
		


	}
}