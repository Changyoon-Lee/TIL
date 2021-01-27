from collections import defaultdict, deque
def countCandies(friends_nodes, friends_from, friends_to, friends_weight):
    # Write your code here
    a = defaultdict(lambda : [1,0])
    b = defaultdict(lambda : [0]*(friends_nodes+1))
    for i,j,k in zip(friends_from, friends_to, friends_weight):
        if b[k][i]==0:
            if a[k][-1]<i and a[k][-2]!=i:
                if a[k][-2]<i:
                    a[k][-1]=a[k][-2]
                    a[k][-2] = i
                else :
                    a[k][-1]=i
        if b[k][j]==0:
            if a[k][-1]<j and a[k][-2]!=j:
                if a[k][-2]<j:
                    a[k][-1]=a[k][-2]
                    a[k][-2] = j
                else :
                    a[k][-1]=j
    max=0
    for i in range(1, len(a)+1):
         if max<a[i][0]*a[i][1]:
            max = a[i][0]*a[i][1]
    return max   
print(countCandies(4, [3,1,1,2], [3,3,3,3], [3,1,2,2]))