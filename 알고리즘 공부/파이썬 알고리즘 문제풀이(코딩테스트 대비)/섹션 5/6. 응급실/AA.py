import sys
sys.stdin = open('섹션 5/6. 응급실/in2.txt')
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [(a[i],i) for i in range(n)]

cnt = 0
while True:
    k = a.pop(0)
    b= a
    b.sort(reverse=True)
    if k[0]<b[0][0]:
        a.append(k)
        
    else :
        cnt+=1    

        if k[1]==m:
            print(cnt)
            break
