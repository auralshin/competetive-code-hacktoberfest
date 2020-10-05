#include<stdio.h>
#define max1 10
#define max2 10

int main()
{
	int a[max1],b[max2],i,n,m;
	printf("Enter size of 1st array: ");
	scanf("%d",&n);
	printf("Enter the elements of 1st array\n");
	for(i=0;i<n;i++) {
		printf("The array element %d: ",i+1);
		scanf("%d",&a[i]);
	}
	printf("\nEnter the size of 2nd array: ");
	scanf("%d",&m);
	printf("Enter the elements of 2nd array\n");
	for(i=0;i<m;i++) {
	printf("The array element %d: ",i+1);
	scanf("%d",&b[i]);
	}

	for (i=0; i<=m-1;i++)
		a[i+n]=b[i];
	n=n+m;
	printf("\nThe merged elements are:\n");
	for(i=0;i<n;i++)
		printf("%d ",a[i]);
    return 0;
}
