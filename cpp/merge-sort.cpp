#include <iostream>
#include <cstdlib>
using namespace std;

void imp(int x[],int ini,int n); 
void mSort(int *A,int n);
void merge(int *izq,int nIzq,int *der,int nDer,int *A);

int main()
{
 int lista[] = {1,2,5,6,8,10,58,69,2,5,48,7};
 int n = sizeof(lista) / sizeof(int);
 /*
 NOTE: sizeof doesn't return the correct value inside the function because it just sends the direction of the beginning of the array.
 */
 cout<<"  Before the merge sort: ";
 imp(lista,0,n);
 mSort(lista,n);
 cout<<"After the merge sort: ";
 imp(lista,0,n);
 return 0;
}

void imp(int x[],int ini,int n)
{
 for(int i=ini;i<n;i++)
  cout<<x[i]<<" ";
 cout<<endl;
}

void mSort(int *A,int n)
{
 if(n==1){return;}
 int mitad = n / 2;
 int *izq = new int[mitad];
 int *der = new int[n-mitad];
 for(int i=0;i<mitad;i++)
  izq[i] = A[i];
 for(int i=mitad;i<n;i++)
  der[i-mitad] = A[i];
 mSort(izq, mitad);
 mSort(der, n-mitad);
 merge(izq, mitad, der, n-mitad, A);
}

void merge(int *izq,int nIzq,int *der,int nDer,int *A)
{
 int i=0,j=0,k=0;
 while( ( i < nIzq ) && ( j < nDer ) )
 {
  if( izq[i] <= der[j])
  {
   A[k] = izq[i];
   i++;
  }
  else
  {
   A[k] = der[j];
   j++;
  }
  k++;
 }
 while(i < nIzq)
 {
  A[k] = izq[i];
  i++;k++;
 }
 while(j < nDer)
 {
  A[k] = der[j];
  j++;k++;
 }
}
