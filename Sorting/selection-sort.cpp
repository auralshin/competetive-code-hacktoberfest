#include<bits/stdc++.h>
using namespace std;

void selectionsort(int [],int );

int main()
{
	int n;
	printf("Enter the size of the array: ");
	cin>>n;	//array size
	int a[n],i;
	printf("Enter the array elements:\n");
	for(i=0;i<n;i++)
	{
		cin>>a[i];
	}
	selectionsort(a,n);	//function declaration- arguments array and size
	printf("The sorted elements: ");
	for(i=0;i<n;i++)
	{
		cout<<a[i]<<"\t";
	}
	return 0;
}

void selectionsort(int a[],int n)
{
	int min,i,j,temp;
	for(i=0;i<n;i++)
	{
		min=i;	//take min=first index position
		for(j=i+1;j<n;j++)
		{
			if(a[j]<a[min])
			{
				min=j;	//take index position of new small element
			}
		}
		temp=a[i];	//swap new small element with new one
		a[i]=a[min];
		a[min]=temp;
	}
	
}

