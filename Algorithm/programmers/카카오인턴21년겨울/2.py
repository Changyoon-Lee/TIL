from collections import deque

def requestsServed(timestamp, top):
    # Write your code here
    
    Q = deque(timestamp)
    n=len(Q)
    top.sort()
    for t in top:
        tempq=deque()
        cnt=0        
        
        while cnt<5 and Q:
            tempval = Q.pop()
            if tempval<=t:
                cnt+=1
                continue
            else: 
                tempq.appendleft(tempval)

            
        Q=Q+tempq

    return n-len(Q)
                    
print(requestsServed([27, 2, 55, 17, 31, 5, 58, 43, 15, 20, 33, 57, 4, 34, 28, 4, 55, 29, 37, 30, 2, 43, 29, 18, 44], [44, 7, 21, 20, 34]))
################ 다른방식으로 풀이 ############# 근데 둘다 한문제씩 시간초과 된듯
