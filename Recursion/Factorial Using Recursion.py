factorial = 1

def fact(num):
    if(num >= 1):
        return(num * fact(num-1))
    else:
        return(1)
        
# check if the number is negative, positive or zero
num = int(input("Enter Int Number: "))
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:       
   factorial = fact(num)
   print("The factorial of",num,"is",factorial)
