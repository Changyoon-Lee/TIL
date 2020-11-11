import sys
sys.stdin = open('섹션 7/2. 휴가/in1.txt')

def DFS(l, sum):
    global res
    if l==n+1:
        if res<sum:
            res=sum
    else:    
        if l+time[l]<=n+1:
            DFS(l+time[l], sum+pay[l])
        DFS(l+1, sum)



if __name__=='__main__':
    n = int(input())
    time=[0]
    pay=[0]
    for _ in range(n):
        t, p = map(int, input().split())
        time.append(t)
        pay.append(p)
    
    res = 0
    DFS(1,0) #l 이랑 time
    print(res)