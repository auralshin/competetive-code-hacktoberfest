# function for finding factorial

import copy
def factorial(n):
    fact=1
    while(n>1):
        fact=n*factorial(n-1)
        return fact
    return fact

# Checking if number provided is Krishnamurthy number or not.
# if sum of factorial of each digit of given number is equals to the number ,it is Krishnamurthy number.


def checkKrishnamurthy(num):
    temp=copy.deepcopy(num)
    sum=0
    while(num>0):

        rem=num%10
        sum+=factorial(rem)
        num//=10
    if(temp==sum):
        return True
    return False



number=int(input("Enter a number to check whether the number is Krishnamurty or not :-"))
results=checkKrishnamurthy(number)
if(results):
    print("The number {0} is Krishnamurthy number.".format(number))
else:    
    print("The number {0} is not Krishnamurthy number.".format(number))
