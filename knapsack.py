d={}                        #for top down table
if __name__=="__main__":
    wt=list(map(int,input("Enter weight=").strip().split()))
    val=list(map(int,input("entern values=").strip().split()))
    w=int(input("Enter sack size="))
    n=len(wt)

    #{
    # wt- weight array
    # val- value array
    # w- total size of knapsack
    # }
    #base condition
    for i in range(0,n+1):
        for j in range(0,w+1):
            if i==0 or j==0:
                d[(i,j)]=0

        #check condition table
            #if w1<=w then 2 conditon either we take it or omit it
                # if we take it then (n-1,w-w1 is called)  
                #if we omit it then (n-1,w is called)
            #if w1>w then we have to omit it becoz there is no space in knapsack
                #again call (n-1,w)

    for i in range(1,n+1):
        for j in range(1,w+1):
            if abs(wt[i-1])<=j:
                d[(i,j)]=max(val[i-1]+d[(i-1,j-abs(wt[i-1]))],d[(i-1,j)])
            else:
                d[(i,j)]= d[(i-1,j)]
    print("max profit=",d[n,w])