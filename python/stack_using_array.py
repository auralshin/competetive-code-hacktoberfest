''' Stack using array '''

class Stack:
    def __init__(self):
        self.top = -1
        self.MAX = 10
        self.stArray = []

    def push(self):
        if(self.top == self.MAX-1):
            print("OVERFLOW")
        else:
            n = int(input("Enter the value to be pushed: "))
            self.top += 1
            self.stArray.append(n)
            print(n, "pushed at ", self.top)

    def pop(self):
        if(self.top == -1):
            print("UNDERFLOW")
        else:
            val = self.stArray.pop()
            self.top -= 1
            print(val, "popped from the stack")

    def peek(self):
        if(self.top == -1):
            print("UNDERFLOW")
        else:
            print("Stack top element is: ", self.stArray[self.top])

    def display(self):
        if(self.top == -1):
            print("UNDERLOW")
        else:
            print(self.stArray[::-1])

if __name__ == '__main__':
    st = Stack()
    while(1):
        print("Enter 1 to PUSH\nEnter 2 to POP\nEnter 3 to PEEK\nEnter 4 to DISPLAY\nEnter 5 to EXIT\n")
        switcher = {
            1: st.push,
            2: st.pop,
            3: st.peek,
            4: st.display,
            5:exit}
        print("Enter your choice: ")
        func = switcher.get(int(input()), "Error!")
        func()
        
