import math
def calpos(n,k):
    if(n==1):
        return 1
    else:
        return (calpos(n-1,k)+(k-1))%n + 1

for _ in range(int(input())):
    n=int(input("Enter the number of person: "))
    k=int(input("Enter the removing position: "))

    if(n==1):
        print("The safe position is: ",n)

    elif(k==2):
        position=(2*n)-(2**(1+math.floor(math.log10(n)/math.log10(2))))+1
        print("The safe position is: ",position)
    else:
        print("The safe position is: ",calpos(n,k))
