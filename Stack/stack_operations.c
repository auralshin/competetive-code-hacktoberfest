 #include<stdio.h>
 void main()
 {  int top1=-1,top2,i,n,a[50],ch,data,p,opt;
    printf("\nEnter the number of elements in stack");
    scanf("%d",&n);
    top2=n;
    do
    {   printf("\nOptions:\n1.Stack1\n2.Stack2");
        printf("\nEnter option:");
        scanf("%d",&opt);
        printf("\nMenu\n");
        printf("\n1.Push\n2.Pop\n3.Peep\n4.Is empty\n5.Is full\n6.Display\n7.Exit");
        printf("\nEnter your choice:");
        scanf("%d",&ch);
        if(ch==1)
        {   if(opt==1)
            {if(top1+1==top2)
                printf("\nStack1 Overflow");
            else
            {   top1++;
                printf("\nEnter the value to be added:");
                scanf("%d",&data);
                a[top1]=data;}}
            else
            {if(top2-1==top1)
                printf("\nStack2 Overflow");
            else
            {   top2--;
                printf("\nEnter the value to be added:");
                scanf("%d",&data);
                a[top2]=data;}}
        }
        else if(ch==2)
        {   if(opt==1)
            {if(top1==-1)
                printf("\n Stack1 Underflow");
            else
            {  p=a[top1];
            top1--;
            printf("Popped elements=%d",p);}}
            else
            {if(top2==n)
                printf("\nStack2 Underflow");
            else
            {p=a[top2];
            top2++;
            printf("Popped elements=%d",p);}}
        }
        else if(ch==3)
        {   if(opt==1)
            {if(top1==-1)
                printf("\nStack1 underflow");
            else{
                printf("\nTop most element:%d",a[top1]);}}
            else
            {if(top2==n)
            printf("\nStack2 underflow");
            else{
            printf("\nTop most element:%d",a[top2]);}}
        }
        else if(ch==4)
        {   if(opt==1)
            {if(top1==-1)
                printf("\nStack1 is empty");
            else
                printf("\nStack1 is not empty");}
            else
            {if(top2==n)
            printf("\nStack2 is empty");
            else
            printf("\nStack2 is not empty");
            }
        }
        else if(ch==5)
        {   if(opt==1)
            {if(top1+1==top2)
                printf("\nStack1 is full");
            else
            printf("\nStack1 is not full");}
            else
            {if(top2-1==top1)
                printf("\nStack2 is full");
            else
                printf("\nStack2 is not full");}
        }
        else if(ch==6)
        {   if(opt==1)
            {if(top1==-1)
                printf("\nStack1 Underflow");
            else
            {printf("\nOutput Stack1:\n");
            for(i=0;i<=top1;i++)
            printf("\t%d",a[i]);}}
            else
            {if(top2==n)
                printf("\nStack2 Underflow");
            else
            {printf("\nOutput Stack2:\n");
            for(i=n-1;i>=top2;i--)
            printf("\t%d",a[i]);}}
        }
    }while(ch<7);
 }
                                             
