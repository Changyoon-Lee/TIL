import sys
sys.stdin = open('섹션 7/8. 사과나무/in1.txt')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ch = [[0]*n for _ in range(n)]
sum=0

ch[n//2][n//2]=1
sum+=a[n//2][n//2]
Q=[]
L=0
Q.append((n//2,n//2))

while True:
    if L==n//2:
        break
    size=len(Q)
    else:
        for i in range(size):
            tmp=Q.pop(0)
            for j in range(4):
                x=tmp[0]+dx[j]
                y=tmp[1]+dy[j]
                if ch[x][y]==0:
                    sum+=a[x][y]
                    ch[x][y]=1
                    Q.append((x,y))

    L+=1
        
