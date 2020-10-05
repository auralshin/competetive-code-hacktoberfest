def GCD(number1,number2): 
    if(number2==0): 
        return number1 
    else: 
        return GCD(number2,number1%number2)
a=12
b=20
print(GCD(a,b))