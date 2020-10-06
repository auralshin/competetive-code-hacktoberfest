#include <stdio.h>
int iterative_binary(int array[], int start, int end, int search);
int main()
{
    int array[50], n, i, s;
    int idx;
    printf("How many elements do you want to enter? ");
    scanf("%d",&n);
    
    printf("Enter %d elements:\n",n);
    for(i=0;i<n;i++)
    {
        scanf("\t%d",&array[i]);
    }
    
    printf("Enter the element to search: ");
    scanf("%d",&s);

    idx = iterative_binary(array, 0, n-1, s);
    if(idx == NULL)
    {
        printf("Element is not present in the array.\n");
    }
    else
    {
        printf("The element occurs in index: %d\n",idx);
    }
    return 0;
}

int iterative_binary(int array[], int start, int end, int search)
{
   while (start <= end)
   {
      int mid = start + (end - start)/2;
      printf("Middle element: %d\n",mid);
      if (array[mid] == search)
         return mid;
      if (array[mid] < search)
         start = mid + 1;
      else
         end = mid - 1;
   }
   return;
}














