import sys
sys.stdin = open('섹션 4/4. 마구간 정하기/in5.txt')

n, c = map(int, input().split())
numlist = [int(input()) for _ in range(n)]
numlist.sort()

lt=0
rt=numlist[-1]
mid = (lt+rt)//2

while lt<=rt:
    temp=0
    cnt=1
    
    for i, val in enumerate(numlist):
        if i==0:
            temp=val
        else : 
            if val-temp >= mid:
                cnt+=1
                temp = val
            else : pass
    if cnt < c:
        rt = mid-1
    else:
        lt = mid+1
    mid = (lt+rt)//2
        
print(mid)
