def splitIntoTwo(arr):
    # Write your code here
    l_sum = 0
    r_sum = sum(arr)
    cnt=0

    for i in range(len(arr)-1):
        l_sum+=arr[i]
        r_sum-=arr[i]
        if l_sum > r_sum:
            cnt+=1
    return cnt
        
