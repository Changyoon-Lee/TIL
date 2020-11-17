import sys
sys.stdin = open('섹션 7/9. 미로의 최단거리 통로/in1.txt')

Q = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = 7
a = [list(map(int, input().split())) for _ in range(7)]

ch=[[0]*n for _ in range(7)]
ch[0][0]=1
L=0

Q.append((0,0))

while Q:
    tmp=Q.pop(0)
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and ch[x][y]==0:
            ch[x][y] = 1
            a[x][y]=a[tmp[0]][tmp[1]]+1
            Q.append((x,y))

if a[6][6] == 0:
    print(-1)
print(a[6][6])