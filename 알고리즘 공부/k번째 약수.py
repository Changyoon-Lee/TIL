import sys
# sys.stdin=open('/TIL/알고리즘 공부/파이썬 알고리즘 문제풀이(코딩테스트 대비)\섹션 2\1. k번째 약수/in1.txt','rt')
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