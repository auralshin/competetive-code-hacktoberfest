// This code is showing stack and it's operation using linked list

#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

void linkedListtraversal(Node *ptr)
{
    while (ptr != NULL)
    {
        cout << "Element : " << ptr->data << endl;
        ptr = ptr->next;
    }
}

int IsEmpty(Node *top)
{
    if (top == NULL)
    {
        return 1;
    }

    else
    {
        return 0; 
    }
     
}

int isFull(Node *top)
{
    Node *p = new Node();

    if (p == NULL)
    {
        return 1;
    }

    else
    {
        return 0;
    }
    
}

Node *push(Node *top, int x)
{

    if (isFull(top))
    {
        cout << "Stack Overflow!!!!" << endl;
        exit(0);
    }

    else
    {
        Node *n = new Node();

        n->data = x;
        n->next = top;
        top = n;
        return top;
    }
}

int pop(struct Node **top)
{
    if (IsEmpty(*top))
    {
        cout << "Stack Underflow!!!!";
        exit(0);
    }

    else
    {
        struct Node *n = *top;
        *top = (*top)->next;
        int x = n->data;
        delete n;
        return x;
    }
}

int main()
{
    Node *top = NULL;

    top = push(top, 78);
    top = push(top, 7);
    top = push(top, 8);

    linkedListtraversal(top);

    int element = pop(&top);
    cout << "\nPopped element is "<< element<<endl;
    linkedListtraversal(top);

    return 0;
}
