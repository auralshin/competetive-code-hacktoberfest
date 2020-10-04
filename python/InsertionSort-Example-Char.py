def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      # i-1 element assigning
      j = i-1
      while j >=0 and key < arr[j] :
         arr[j+1] = arr[j]
         j -= 1
      arr[j+1] = key
# sorting characters
arr = ['t','u','t','o','r','i','a','l']
insertionSort(arr)
print ("Result: ")
for i in range(len(arr)):
   print (arr[i])
