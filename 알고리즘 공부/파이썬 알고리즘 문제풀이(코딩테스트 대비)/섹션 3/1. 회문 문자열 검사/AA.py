import sys
# sys.stdin = open('섹션 3/1. 회문 문자열 검사/in1.txt')

n = int(input())
cn = 0
for i in range(n):
    cn +=1
    a = input().lower()
    if a == a[::-1]:
        print(f'#{cn} YES')
    else :
        print(f'#{cn} NO')