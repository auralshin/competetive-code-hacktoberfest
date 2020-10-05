def MergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Finding the mid of the array 
        left = arr[:mid] # Dividing the array elements  
        right = arr[mid:] # into 2 halves 
        MergeSort(left) # Sorting the first half 
        MergeSort(right) # Sorting the second half 
        i = j = k = 0
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+= 1
            else: 
                arr[k] = right[j] 
                j+= 1
            k+= 1
        # Checking if any element was left 
        while i < len(left): 
            arr[k] = left[i] 
            i+= 1
            k+= 1
          
        while j < len(right): 
            arr[k] = right[j] 
            j+= 1
            k+= 1
arr=[1,9,2,8,3,7,4,6,5]
#calling the sort fucnction
MergeSort(arr)
print("The sorted array is:")
print(*arr)
print("The time complexity is O(nlogn)")