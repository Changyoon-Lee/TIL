import sys
sys.stdin = open('섹션 7/1. 최대점수 구하기/in2.txt')

def DFS(l, sum, time):
    global res

    if l>=n or time>m:
        return
    if res<sum:
        res = sum
    DFS(l+1, sum+pv[l], time+pt[l])
    DFS(l+1, sum, time)



if __name__=='__main__':
    n, m = map(int, input().split())
    pv=[]
    pt=[]
    for _ in range(n):
        v, t = map(int, input().split())
        pv.append(v)
        pt.append(t)
    
    res = 0
    DFS(0,0,0)
    print(res)