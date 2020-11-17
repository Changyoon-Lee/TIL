def solution(prices):
    n = len(prices)
    time = [0]*n
    sdic={}
    k=0
    last = 0
    while n!=0:
        
        n-=1
        temp = prices.pop()
        if temp>last:
            time[n]=k
            sdic[last]=sdic.get(last,0)+k+1
            k=0
        else : 
            k+=1
            time[n]=k+sdic.get(temp,0)
        last = temp
        
    return time

solution([1, 2, 3, 2, 3])