#Contribution by David Lazaro Fernandez
# Shell sort in python

#Sorting Function
def shellSort(array, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    #We're going to continue sorting until the interval be = 0
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

#The name of our array
data = [9, 8, 3, 7, 5, 6, 4, 1]
#The size of the array
size = len(data)
print('Our array before being sorted')
print(data)
#Calling of the sorting function
shellSort(data, size)
#Finally we print the Sorted array
print('Sorted Array in Ascending Order:')
print(data)
