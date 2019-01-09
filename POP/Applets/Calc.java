import java.awt.*;
import java.applet.*;
import java.awt.event.*;


public class Calc extends Applet implements ActionListener{

	Button add,subtract,multiply,divide;
	TextField op1,op2,result;


	public void init(){
		setBackground(Color.BLACK);
		setForeground(Color.CYAN);
	


		add=new Button("+");
		add.setSize(200,200);
		add.addActionListener(this);

		subtract=new Button("-");
		subtract.setSize(200,200);
		subtract.addActionListener(this);

		multiply=new Button("*");
		multiply.setSize(200,200);
		multiply.addActionListener(this);

		divide=new Button("/");
		divide.setSize(200,200);
		divide.addActionListener(this);

		op1=new TextField("Enter First Operand Here");
		op2=new TextField("Enter Second Operand here");
		result = new TextField("Result will be displayed here");
		result.setEditable(false);



		add(op1);
		add(op2);
		add(add);
		add(subtract);
		add(multiply);
		add(divide);
		add(result);

		




	}

	public void start(){
		


	}



	public void paint(Graphics g)
	{
		g.drawString("Hello boiss",45,45);


	}

	public void actionPerformed(ActionEvent e)
	{
		int a = Integer.parseInt(op1.getText());
		int b = Integer.parseInt(op2.getText());
		String str = e.getActionCommand();
		char oper=str.charAt(0);	
		double res = 0.0;

		switch(oper){

				case('+'):
					res=a+b;
					break;
				case('-'):
					res=a-b;
					break;
				case('*'):
					res=a*b;					
					break;
				case('/'):
				res=(a*1.0)/b;
										



			}

		String r = Double.toString(res);
	
			result.setText(r);
		

		
	}




	


}