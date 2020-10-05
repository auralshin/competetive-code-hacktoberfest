/*
  The below program shows the full implementation of a stack data structure in C using arrays
*/







#include<stdio.h>
#include<stdlib.h>
int isEmpty();
int isFull();
void push();
int pop();
void displayStack();
struct Stack{
    int top;
    int totalSize;
    int *ptr;
};
void push(struct Stack * s,int n){
    if(isFull(s)==0){
    s->top+=1;
    s->ptr[s->top]=n;
    }
    else{
        printf("Stack overflow\n");
    }
}

int pop(struct Stack *s){
    if(isEmpty(s)==0){
    int n=s->ptr[s->top];
    s->top-=1;
    return n;
    }
    else{
        printf("Stack underflow\n");
    }
}

void displayStack(struct Stack *s){
    for (int i = 0; i<=s->top; i++){
        printf("%d\n",s->ptr[i]);
    }
}

int isFull(struct Stack *s){
    if(s->top==(s->totalSize)-1){
        return 1;
    }
    else{
        return 0;
    }
}

int isEmpty(struct Stack *s){
    if(s->top==-1){
        return 1;
    }
    else{
        return 0;
    }
}
int main(){
    struct Stack *s=(struct Stack *)malloc(sizeof(struct Stack));
    s->top=-1;
    s->totalSize=80;
    s->ptr=(int *)malloc(s->totalSize*sizeof(int));
    pop(s);
    push(s,2);
    displayStack(s);
}
