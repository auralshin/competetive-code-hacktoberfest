''' Stack using Linked List '''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.top = None

    def push(self):
        n = int(input("Enter the value to be pushed: "))
        newNode = Node(n)
        if(self.top == None):
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        print("Pushed")

    def pop(self):
        if(self.top == None):
            print("UNDERFLOW")
        else:
            pNode = self.top
            self.top = self.top.next
            pNode.next = None
            print(pNode.data, "popped from the stack")

    def peek(self):
        if(self.top == None):
            print("UNDERFLOW")
        else:
            print("Stack top data is: ", self.top.data)

    def display(self):
        st = []
        temp = self.top
        while(temp != None):
            st.append(temp.data)
            temp = temp.next
        print(st)

if __name__ == "__main__":
    llist = LinkedList()
    while(1):
        print("Enter 1 to PUSH\nEnter 2 to POP\nEnter 3 to PEEK\nEnter 4 to DISPLAY\nEnter 5 to EXIT")
        switcher = {
                1: llist.push,
                2: llist.pop,
                3: llist.peek,
                4: llist.display,
                5: exit
            }
        print("Enter your choice: ")
        func = switcher.get(int(input()), "ERROR!")
        func()
