import sys
import heapq as hq
sys.stdin = open('섹션 5/10. 최소힙/in1.txt')

a = []
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)