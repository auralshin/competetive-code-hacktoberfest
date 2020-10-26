// program to search an element in an array
// using the linear search technique.(used for Unsorted Arrays)

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#define maxsize 20  // Added so the size of the array can be altered more easily


//Function to print an array
void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}


// main function
int main()
{
    int arr[maxsize], num, i, size, found = 0, pos = -1;

    printf("\n Enter the number of elements in the array : ");
    scanf("%d", &size);
    printf("\n Enter the elements: ");
    for(i=0;i<size;i++)
    {
        scanf("%d", &arr[i]);
    }
    printf("\n Entered array is : ");
    printArray( arr, size);

    printf("\n\n Enter the number that has to be searched : ");
    scanf("%d", &num);
    for(i=0; i<size; i++)
    {
        if(arr[i] == num)
        {
            found = 1;
            pos=i;
            printf("\n %d is found in the array at position = %d", num, i+1);

/* +1 added in line 23 so that it would display the number in
 the first place in the array as in position 1 instead of 0 */

            break;

        }
    }

    if (found == 0)
        printf("\n %d does not exist in the array!", num);
    return 0;

}
