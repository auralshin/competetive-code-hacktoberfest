#Contribution by David-Lazaro-Fernandez
#Quick-Sort algorithm in python 

#This will be the list we're gonna work with
myList = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36]

#Sorting Funtcion 
def sort(list):

    #Basically we're gonna divide our array in 3 parts: left, center and right 
    #The center will be our pivot. All the elements in the array who are < to pivot will be in the 'left' array
    #All the elementes in the array who are > to the pivot will be in the 'right' array.
    #We're gonna call this function until all the elements in the array are sorted. 
    left = []       
    center = []
    right = []
    if len(list) > 1:
        pivot = list[0]
        for i in list:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                center.append(i)
            elif i > pivot:
                right.append(i)
        #print(left+["-"]+center+["-"]+right)
        return sort(left)+center+sort(right)
    else:
      return list
#Then we print the list before being sorted
print(myList)
#And finally the list after being sorted
print(sort(myList))
