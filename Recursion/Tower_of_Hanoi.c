// This code is contributed by @harshest2019

// This Code takes number of disks as input and performs tower of hanoi over three pegs.

// The basic idea is you have to perform Tower of Hanoi on n-1 disks recursively reaching to 1 disk.

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void toh(char ini,char dest,char mid,int n);
int main(){
    char a='A',b='B',c='C';
    int rods;
    scanf("%d",&rods);
    toh(a,b,c,rods);
}

void toh(char ini,char dest,char mid,int n){
    if(n==2){
        printf("Move disk %d from %c to %c \n",n-1,ini,mid);
        printf("Move disk %d from %c to %c \n",n,ini,dest);
        printf("Move disk %d from %c to %c \n",n-1,mid,dest);

    }
    else{
        
        // We shift n-1 disk from Initial Peg to Intermediate Peg
        
        toh(ini,mid,dest,n-1);
        
        // We shift nth disk from Initial Peg to Final Peg
        
        printf("Move disk %d from %c to %c \n",n,ini,dest);
        
        // Reshifting n-1 disk from Intermediate peg to Final Peg
        
        toh(mid,dest,ini,n-1);
}
}