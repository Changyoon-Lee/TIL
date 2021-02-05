# DFS하려다가 오래걸릴거같아서 안함

def solution(triangle):
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            if triangle[i+1][j]>triangle[i+1][j+1]:
                triangle[i][j] += triangle[i+1][j]
            else :
                triangle[i][j] += triangle[i+1][j+1]
    return triangle[0][0]