#fractional knapsack problem
class itemdata:
    def __init__(self,wt,val,ind):
        self.wt=wt
        self.val=val
        self.ind=ind
        self.cost=val//wt
        
    def __lt__(self,other):
        return self.cost<other.cost

class FractionalKnapsack:
    def getmaxval(wt,val,cap):
        ith_val=[]
        for i in range(len(wt)):
            ith_val.append(itemdata(wt[i], val[i],i))
        ith_val.sort(reverse=True)
        total=0
        for i in ith_val: 
            curwt=i.wt
            curval=i.val
            if (cap-curwt)>=0:
                total+=curval
                cap-=curwt
            else:
                fraction=cap/curwt
                total+=(curval*fraction)
                cap-=(curwt*fraction)
                break
        return total
    
if __name__=="__main__":
    print("Enter the weights you have: ")
    wt=list(map(int, input().split()))
    print("Enter the value of corresponding weight: ")
    val=list(map(int,input().split()))
    print("Enter the capacity of the knapsack: ")
    cap=int(input())
    maxval=FractionalKnapsack.getmaxval(wt,val,cap)
    print("Maximum value in knapsack: ",maxval)
