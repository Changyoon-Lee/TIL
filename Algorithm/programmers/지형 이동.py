# 코딩테스트 연습 > Summer/Winter Coding(2019) > 지형이동

                
# def DFS2lather():


def solution(land, height):
    def DFS(i,j):
        nonlocal n, dx, dy, land, board, height, mark
        board[i][j] = mark # board에 체크  1이면 방문한것, 0이면 방문 안한것
        for k in range(4):
            if 0<= i+dx[k] < n and 0<= j+dy[k] < n: #인덱스가 존재하면
                if board[i+dx[k]][j+dy[k]]==0 and abs(land[i+dx[k]][j+dy[k]]-land[i][j]) <= height: # 방문 안했고, 이동가능하다면
                    DFS(i+dx[k], j+dy[k])

    mark = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    n = len(land)
    board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                mark+=1
                DFS(i,j)
                 # 구역이 다르면 marking 다른걸로 하기위해 1더함


    lather=[[0]*mark for _ in range(mark)]
    dx = [1, 0]
    dy = [0, 1]
    for i in range(n):
        for j in range(n):
            for k in range(2):
                if 0<= i+dx[k] < n and 0<= j+dy[k] < n:
                    a = board[i][j]-1
                    b = board[i+dx[k]][j+dy[k]]-1
                    if a!=b:
                        if lather[a][b]==0 or lather[a][b] > abs(land[i+dx[k]][j+dy[k]]-land[i][j]):
                            lather[a][b]=abs(land[i+dx[k]][j+dy[k]]-land[i][j])
                            lather[b][a]=lather[a][b]


    cost = 0
    marked=[0]*mark
    
    for i in range(mark):
        mi=0
        idx_j=0
        if marked[i]==0:
            for j in range(mark):
                if lather[i][j]!=0:
                    if mi==0:
                        mi = lather[i][j]
                        idx_j=j
                    elif mi > lather[i][j]:
                        mi=lather[i][j]
                        idx_j=j
            marked[i]=1
            marked[idx_j]=1
            cost+=mi



    return cost

print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],1))

