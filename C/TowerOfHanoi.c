#include<stdio.h>
void tower(int,int,int,int);

int main()
{
	int n;

	printf("\nenter the number of discs:");
	scanf("%d",&n);

	printf("moves:\n");

	tower(n,1,2,3);//calling the tower function

	return 0;
}
void tower(int n,int fr,int to,int spr)//recursive function
{
	if(n==1)//base condition
	{
	printf("move from %d to%d\n",fr,to);
	return;
	}
	else
	{
	tower(n-1,fr,spr,to);
	tower(1,fr,to,spr);
	tower(n-1,spr,to,fr);

	}
}