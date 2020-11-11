import sys
# sys.stdin = open('섹션 4/6. 씨름선수/in1.txt')

n = int(input())

a = [tuple(map(int, input().split())) for _ in range(n)]

a.sort(reverse=True,key=lambda x:(x[0],x[1]))
temp=0
cn=0
for i in a:
    if i[1]>temp:
        cn+=1
        temp = i[1]

print(cn)