# Bubble Sorting Algorithm

def Bubble_Sort(A,n):
    for k in range(1,n):
        for i in range(0,n-1):
            if(A[i]>A[i+1]):
                A[i],A[i+1]=A[i+1],A[i]

if __name__=="__main__":
    print("Enter the elements in the array: ")
    A=[]
    A=list(map(int,input().split(" ")))
    n=len(A)
    Bubble_Sort(A,n)
    print("Sorted Array: ",end="")
    for i in range(0,n):
        print(A[i],end=" ")

# Time Complexity: O(n^2)
# Space Complexity: O(1)