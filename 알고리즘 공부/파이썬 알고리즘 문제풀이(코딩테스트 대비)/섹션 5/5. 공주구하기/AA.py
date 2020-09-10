import sys
# sys.stdin = open('섹션 5/5. 공주구하기/in1.txt')

n, k = map(int, input().split())

que = list(range(1,n+1))
i=0
while len(que)!=1:
    i+=1
    if i%k==0:
        que.pop(0)
    else :
        que.append(que.pop(0))

print(que[0])
        