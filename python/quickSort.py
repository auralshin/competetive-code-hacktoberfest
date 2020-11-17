# Quicksort
# Best case: O(n)
# Average case: O(n log n)
# Worst case: O(n^2) 

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        piv = arr.pop()
        less_arr = []
        greater_arr = []

        for element in arr:
            if element < piv:
                less_arr.append(element)
            else:
                greater_arr.append(element)
        
        return quick_sort(less_arr) + [piv] + quick_sort(greater_arr)

# Example
print(quick_sort([3,5,6,63,2,4,6765,423,234,2334,3,3,2,1,5,6,8,9,423,6]))