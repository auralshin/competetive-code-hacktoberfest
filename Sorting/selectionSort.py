# Selection Sorting Algorithm

def SelectionSort(A,n):
    for i in range(0,n-1):
        iMin=i
        for j in range(i+1,n):
            if(A[j]<A[iMin]):
                iMin=j
        #temp=A[i]
        #A[i]=A[iMin]
        #A[iMin]=temp
        A[i],A[iMin]=A[iMin],A[i]

if __name__=="__main__":
    
    A=[]
    print("Enter the elements in array:")
    A=list(map(int,input().split(" ")))
    #A=[3,7,1,8,0,5]
    n=len(A)
    print(n,A)
    SelectionSort(A,n)
    for j in range(0,n):
        print(A[j],end=" ")

# Time complexity: O(n^2)
# Space complexity: O(1)
