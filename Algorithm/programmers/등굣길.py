def solution(m, n, puddles):
    board = [[0]*(m+1) for _ in range(n+1)]
    chk = {(puddle[1], puddle[0]):True for puddle in puddles}
    
    #board 에 puddles 정보 1로 표기, x,y좌표형식을 행열로 변환하기위해 변경
    board[1][1]=1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if chk.get((j,i)) or (i==j==1): continue
            else : board[j][i]=(board[j-1][i]+board[j][i-1])%1000000007

    return board[n][m]

print(solution(4,3,[[2, 2]]))