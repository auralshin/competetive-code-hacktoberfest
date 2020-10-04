'''
The way this algorithm works is 
first we define a pivot point as a reference we can use any point as a 
reference but here we are using last value from our input list

and then we make two list namesd as lower and heigher and we append value 
respective to the pivot point to the respective list 

and we done the same process over and over again till the condition breaks 
'''

def quick_short(List):
    length = len(List)
    lower = []
    heigher = []
    if length <= 1:
        return List
    else:
        pivot = List.pop()
    for i in List:
        if i >= pivot:
            heigher.append(i)
        else:
            lower.append(i)
    return quick_short(lower) + [pivot] + quick_short(heigher)

x = quick_short([
89,399,757,257,372,553,241,216,48,355,41,34,798,470,751,285,288,768,563,2,638,113,153,394,500,715,495,217,578,625,628,27,345,329,579,677,331,211,354,646,715,595,784,552,515,226,598,533,508,332,515,789,521,261,117,415,712,604,93,144,595,38,423,798,165,472,573,771,312,330,92,731,775,579,140,329,530,439,276,166,395,233,41,314,141,201,688,383,763,606,87,672,207,564,687,285,24,216,394,675,652,302,33,786,540,173,664,624,58,190,792,43,178,212,557,231,389,641,586,504,301,92,573,126,85,678,27,480,765,637,255,193,300,693,74,16,146,479,54,87,503,215,161,208,673,83,180,520,591,786,559,486,12,
])
x = set(x) 
print(x)

