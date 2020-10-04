# Python program for implementation og Bubble Sort
# Making Function to perform bubbleSort
def bubbleSort(arrays):
    for passnum in range(len(arrays)-1, 0, -1):
        for i in range(passnum):
            if arrays[i] > arrays[i+1]:
                temp = arrays[i]
                arrays[i] = arrays[i+1]
                arrays[i+1] = temp


# initialize the array
arrays = [5, 2, 9, 1, 7, 3, 4, 505, 200]
# Performing bubbleSort Function
bubbleSort(arrays)
# Printing array after bubble sort
print(arrays)


# Anotherway of implementing Bubble short inpython

def bubble_short(sequence):
    indexing_length = len(sequence) - 1
    shorted = False

    while not shorted:
        shorted = True
        for i in range(indexing_length):
            if sequence[i] > sequence[i+1]:
                shorted = False
                sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
    return sequence


print(bubble_short([89, 399, 757, 257, 372, 553,
                    241, 216, 48, 355, 41, 34, 798, 470, 751]))
