import java.applet.*;
import java.awt.*;
import java.awt.event.*;

public class Man extends Applet implements ActionListener
{

	int x1=200, x2=200, y1=150, y2=300;
	int choice = 1;
	Button next, prev, opt,down;

	public void init()
	{
		prev = new Button("Move Back");
		prev.addActionListener(this);
		add(prev);
		next = new Button("Move Front");
		next.addActionListener(this);
		add(next);
		opt = new Button("Fly");
		opt.addActionListener(this);
		add(opt);


		down=new Button("Down");
		down.addActionListener(this);
		add(down);
	}

	public void paint(Graphics g)
	{
		
		g.drawLine(x1,y1,x2,y2);
			
			g.drawLine(x1, y1+50, x2+75, y1-20); //right side hand
			g.drawLine(x1-75, y1-20, x2, y1+50); //left
		
		
		g.drawLine(x2, y2, x2+75, y2+75); //right side leg
		g.drawLine(x2-75,y2+75, x2, y2); //left

		g.drawArc(x1-35, y1-70, 70, 70, 0, 360);
		
		
		g.drawArc(x1-22, y1-50, 15, 15, 0, 360);
		g.drawArc(x1+7, y1-50, 15, 15, 0, 360);

		g.drawArc(x1-22, y1-40, 45, 30, 0, -180);
	}

	public void actionPerformed(ActionEvent ae) 
	{
		String str=ae.getActionCommand();
		if (str.equals("Move Front"))
		{	
			x1+=50;
			x2+=50;
			repaint();
		}
		else if (str.equals("Move Back"))
		{
			x1-=50;
			x2-=50;
			repaint();
		}
		else if (str.equals("Fly"))
		{
			// if (choice == 1)
			// 	choice = 2;
			// else if (choice == 2)
			// 	choice = 1;
			


			y1=y1-10;
			y2=y2-10;


			repaint();
			

			

		}

		else if( str.equals("Down")){
			y1+=10;
			y2+=10;
			repaint();
		}
	}
}