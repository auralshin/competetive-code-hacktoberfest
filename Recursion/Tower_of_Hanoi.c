// This code is contributed by @harshest2019
// This Code takes number of disks as input and performs tower of hanoi over three pegs.
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
        toh(ini,mid,dest,n-1);
        printf("Move disk %d from %c to %c \n",n,ini,dest);
        toh(mid,dest,ini,n-1);
}
}