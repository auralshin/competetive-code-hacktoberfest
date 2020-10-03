#HacktoberFest
print('Enter No. of array')
T=int(input())
while T!=0:
    print('Enter no. of elements in the array')
    n=int(input())
    count=0
    print('Enter array elements')
    v=[int(i) for i in input().split()]
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (v[i] > v[j]): 
                count += 1    
    print('No. of Inversions are :', count)
    
    T-=1