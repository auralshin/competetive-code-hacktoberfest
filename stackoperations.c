#include <stdio.h>
#include <stdlib.h>
struct stack
{
    int size;
    int top;
    int *arr;
};

int isEmpty(struct stack *ptr)
{
    if (ptr->top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int isFull(struct stack *ptr)
{
    if (ptr->top == ptr->size - 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int push(struct stack *ptr, int value)
{
    if (isFull(ptr))
    {
        printf("Stack Overflow\n");
    }
    else
    {
        ptr->top++;
        ptr->arr[ptr->top] = value;
    }
}

int pop(struct stack *ptr)
{
    if (isEmpty(ptr))
    {
        printf("Stack Uverflow\n");
        return -1;
    }
    else
    {
        int value = ptr->arr[ptr->top];
        ptr->top--;
        return value;
    }
}

int main()
{
    struct stack *sp = (struct stack *)malloc(sizeof(struct stack));
    sp->size = 10;
    sp->top = -1;
    sp->arr = (int *)malloc(sp->size * sizeof(int));
    printf("stack is created successfully\n");
    printf("before push %d\n", isEmpty(sp));
    printf("before push %d\n", isFull(sp));
    push(sp, 3);
    push(sp, 31);
    push(sp, 23);
    push(sp, 53);
    push(sp, 73);
    push(sp, 663);
    push(sp, 443);
    push(sp, 343);
    push(sp, 213);
    push(sp, 300);
    printf("after push %d\n", isEmpty(sp));
    printf("after push %d\n", isFull(sp));

    printf("poped out element %d\n", pop(sp));
    printf("poped out element %d\n", pop(sp));

    push(sp, 300);
    push(sp, 300);
    push(sp, 300);
    return 0;
}