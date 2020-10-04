// This Header File is contributed by @harshest2019
// Can be used on cpp and c
// Helps in basic matrix functions like Input, Print, Symmetric, Multiplication of matrices,Transpose and Determinant

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void printarr(int n,int m,int (*j)[m]);
void append(int n,int m,int (*j)[m]);
void symmetry(int n,int m,int (*j)[m]);
void transpose(int n, int m, int (*j)[m]);
void multiply(int n,int m,int (*j)[m],int n1, int m1, int (*w)[m1],int (*res)[m1]);
int determ(int order,int(*j)[order]);



void append(int n,int m,int (*j)[m]){
    // Parameters: N and M and N*M 2D array
    // Fills Entries in the matrix
    int i,k;
    for(i=0;i<n;i++){
        for(k=0;k<m;k++){
            scanf("%d",&j[i][k]);
        }
    }
}

void printarr(int n,int m,int (*j)[m]){
    // Parameters: N and M and N*M 2D array
    // Prints the Matrix
    int i,k;
    for(i=0;i<n;i++){
        for(k=0;k<m;k++){
            printf("%d ",j[i][k]);
    
        }
        printf("\n");
    }
}

void transpose(int n, int m, int (*j)[m]){
    // Parameters: N and M and N*M 2D array
    // Prints the Transpose of the Matrix
    int i,k;
    for(i=0;i<m;i++){
        for(k=0;k<n;k++){
            printf("%d ",j[k][i]);

        }
        printf("\n");
    }
}

void symmetry(int n,int m,int (*j)[m]){
    // Parameters: N and M and N*M 2D array
    // Tells whether the matrix is a symmetric matrix or not
    if(n!=m){
        printf("It is not a square matrix \n");
    }
    else{
        int i,k;
        int flag=0;
        for(i=0;i<m;i++){
            for(k=0;k<i;k++){
              if(j[i][k]!=j[k][i]){
                  flag=1;
                 break;
                }
            }        
        }
    
        if(flag==1){
            printf("No, it is not symmetric \n");
        }
        else
            printf("Yes,it is symmetric \n");
    }
}

void multiply(int n,int m,int (*j)[m],int n1, int m1, int (*w)[m1],int (*res)[m1]){
    // Parameters: N and M and N*M 2D array ||| 2 instances of this parameter and 1 2D array to store the answer
    // Multiplies the given matrices

    if(m!=n1){
        printf("Column of first matrix is not equal to rows of second. \n Matrix Multiplication can't be done");
    }
    else{
        int a,b,c;
        for(a=0;a<n;a++){
            for(b=0;b<m1;b++){
                res[a][b]=0;
                for(c=0;c<m;c++){
                    res[a][b]+=(j[a][c]*w[c][b]);
                }
            }
        }

    }
}

int determ(int order, int(*arr)[order]){
    // Parameters:  M and M*M 2D array
    // Return determinant of the given matrix
    if(order==1){
        return arr[0][0];
    }
    else{
        int i;
        int sum=0;
        for(i=0;i<order;i++){
            int c1,c2;
            int norder=0;
            norder=order-1;
            int arr2[norder][norder];
            for(c1=0;c1<norder;c1++){
                int d;
                d=0;
                for(c2=0;c2<norder;c2++){
                    if(d==i){
                        d=d+1;
                        c2--;
                        continue;
                    }
                    else{
                        arr2[c1][c2]=arr[c1+1][d];
                        d++;}
                    }
                }
                sum=sum+pow(-1,i)*arr[0][i]*determ(norder,arr2);
            
            }
            return sum;

        }
    }