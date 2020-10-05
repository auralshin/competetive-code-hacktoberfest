print('Enter an array')
v=[int(i) for i in input().split()]
print('Enter element to be searched')
n=int(input())
for i in v:
    if i==n:
        print('Element found')
        break