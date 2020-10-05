def magic(num):
    """ Checks whether the input num is a magic number or not
    A number is said to be magic number if the sum of its digits summed
    recursively add up to 1
    
    Example : 1234
    1 + 2 + 3 + 4 = 10
    1 + 0 = 1
    """
    sum = 0
    while (num > 0 or sum > 9):
        if (num == 0):
            num = sum
            sum = 0
        sum += num % 10
        num = num // 10
    if (sum == 1):
        return True
    else :
        return False


num = int(input("Enter a number to check for magic number :- "))
result = magic(num)
if(result == True):
    print("The number {0} is magic number.".format(num))
else:
    print("The number {0} is not a magic number".format(num))
