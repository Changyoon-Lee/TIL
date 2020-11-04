import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt=0

    while True:
        
        if scoville[0]>=K:
            return cnt
        if len(scoville)==1:
            return -1

        sum = heapq.heappop(scoville) + 2*heapq.heappop(scoville)
        heapq.heappush(scoville, sum)
        cnt+=1

print(solution([1,2,3,9,10,12], 9))