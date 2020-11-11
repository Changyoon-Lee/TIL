import sys
# sys.stdin = open('섹션 4/10. 역수열/in1.txt')

n = int(input())
a = list(map(int, input().split()))

b = []

for i in a[::-1]:

    b.insert(i, n)
    n-=1

print(' '.join(list(map(str,b))))