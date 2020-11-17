import sys 
def smallestSumSubarr(arr, n): 
    min_ending_here = sys.maxsize 
      
    min_so_far = sys.maxsize 
      
    for i in range(n): 
        if (min_ending_here > 0): 
            min_ending_here = arr[i] 
          
        else: 
            min_ending_here += arr[i] 
           
        min_so_far = min(min_so_far, min_ending_here) 
      
    return min_so_far 
      
arr = [3, -4, 2, -3, -1, 7, -5] 
n = len(arr) 
print(smallestSumSubarr(arr, n))
  