"""
testcase 1:
n = 5
    *
   * *
  * * *
 * * * *
* * * * * 
"""


if __name__ == '__main__':
    n = int(input('Enter the number of rows: ').strip())
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            print(" ", end = "")
        for k in range(1, i+1):
            print("* ", end = "")
        print('\r')
