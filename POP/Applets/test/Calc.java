import java.awt.*;
import java.applet.*;
import java.awt.event.*;


public class Calc extends Applet implements ActionListener{

	Button add,subtract,multiply,divide,equal;
	TextField result;
	Button a[] = new Button[10];
	double var1,var2,ans;
	

	public void init(){
		setBackground(Color.BLACK);
		setForeground(Color.CYAN);
		GridLayout gl=new GridLayout(4,5);
		setLayout(gl);
	


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

		equal=new Button("=");
		equal.addActionListener(this);


		
		result = new TextField("");
		

		for(int i =0;i<10;i++){
			a[i]=new Button(Integer.toString(i));
			
		}


		for(int i =0;i<10;i++){
			a[i].addActionListener(this);
			
		}
		



		add(result);

		for(int i =0;i<10;i++)
			add(a[i]);

		add(add);
		add(subtract);
		add(multiply);
		add(divide);
		add(equal);
		

		




	}

	public void start(){
		


	}



	public void paint(Graphics g)
	{
		
	}

	public void actionPerformed(ActionEvent e)
	{
		String str =e.getActionCommand();
		char ch=str.charAt(0);
		if (Character.isDigit(ch))
		result.setText(t1.getText()+str);
		else

		switch(ch){

				case('+'):
					var1=Double.parseDouble(result.getText());
					break;
				case('-'):
					ans=a-b;
					break;
				case('*'):
					ans=a*b;					
					break;
				case('/'):
					ans=(a*1.0)/b;
					break;

				case('1'):
				case('2'):
				case('3'):
				case('4'):
				case('5'):
				case('6'):
				case('7'):
				case('8'):
				case('9'):
				case('0'):
					a=a*10;
					a=a+Double.parseDouble(oper+"");
					ans=a;


		
			}



		String r = Double.toString(a);
	
			result.setText(r);
		

		
	}




	


}