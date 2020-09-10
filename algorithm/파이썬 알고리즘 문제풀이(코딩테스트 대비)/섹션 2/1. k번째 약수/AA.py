import sys
sys.stdin=open('섹션 2/1. k번째 약수/in1.txt','rt')
n, k = map(int, input().split())

cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1

    if cnt==k:
        print(i)
        break

else:
    print(-1)