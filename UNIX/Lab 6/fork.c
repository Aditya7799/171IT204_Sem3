#include<stdio.h> 


int main() 
{ 
	for(int i=0;i<3;i++) // loop will run n times (n=5) 
	{ 
		
		if(fork() == 0) 
	{ 
			printf("[child] pid %d from [parent] ppid %d\n",getpid(),getppid()); 
			exit(0);
	
			
			
		}
	} 
	 
	
} 





