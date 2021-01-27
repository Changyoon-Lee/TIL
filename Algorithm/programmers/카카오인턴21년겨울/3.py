

    
def segment(x, space):
    # Write your code here
    mx=0
    i=x-1
    n = len(space)
    while i <n:
        if space[i]<=mx:
            i+=x
            continue

        mn=[0, 10**9]
        templist=space[i-x+1:i+1]
        for j in range(x):
            if mn[1]>=templist[j]:
                mn = [j,templist[j]]

        i+=mn[0]+1  
        
        if mx<mn[1]:
            mx=mn[1]
        
        
    return mx
print(segment(3, [1,4,6,2,5,3,6,2,6,3]))
