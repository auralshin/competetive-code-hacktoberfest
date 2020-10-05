//
//  main.c
//  CircularQueue
//
//  Created by Shivam Kejriwal on 25/09/19.
//  Copyright © 2019 Shivam Kejriwal. All rights reserved.
//
#include<stdio.h>
#include<stdlib.h>
#define max 5
void enqueue(void);
void dequeue(void);
void top(void);
void display(void);
int front=-1,rear=-1;
int a[max];
int main()
{
    int ch;
    do{
    printf("\n 1.Insert an Element");
    printf("\n 2.Delete an Element");
    printf("\n 3.Top");
    printf("\n 4.Display The Queue");
    printf("\n 5.Exit");
    printf("\n Enter your choice:");
    scanf("%d",&ch);
    switch(ch)
    {
        case 1:
            enqueue();
            break;
        case 2:
            dequeue();
            break;
        case 3:
            top();
            break;
        case 4:
            display();
            break;
        case 5:
            exit(1);
            break;
        default:
            printf("Invalid Choice");
    }
    }while(ch!=5);
    return 0;
}
void enqueue()
{
    int val;
    printf("\n Enter value of Element");
    scanf("%d",&val);
    if(front==-1 && rear==-1)
    {
        front=0;
        rear=0;
        a[rear]=val;
    }
    else if(front==(rear+1)%max)
    {
        printf("\n Overflow");
    }
    else
    {
        rear=(rear+1)%max;
        a[rear]=val;
    }
}
void dequeue()
{
    int val;
    if(front==-1 && rear==-1)
    {
        printf("\n Underflow");
    }
    else if(front==rear)
    {
        val=a[front];
        printf("%d",val);
        front=-1;
        rear=-1;
    }
    else
    {
        val=a[front];
        printf("%d",val);
        front=(front+1)%max;
    }
}
void top()
{
    if(front==-1&&rear==-1)
    {
        printf("Queue is Empty");
    }
    else
    {
        printf("%d",a[front]);
    }
}
void display()
{
    int i;
    printf("\n");
    if(front==-1&&rear==-1)
    {
        printf("Queue is Empty");
    }
    else
    {
        for(i=front;i!=rear;i=(i+1)%max)
        {
            printf("%d \t",a[i]);
        }
        printf("%d \t",a[rear]);
    }
}
