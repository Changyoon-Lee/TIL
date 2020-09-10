import sys
# sys.stdin = open('섹션 4/8. 침몰하는 타이타닉/in3.txt')

n, m = map(int, input().split())

a = list(map(int, input().split()))
a.sort()
cn=0
while a:
    if a[0]+a[-1]>m:
        a.pop()
        cn+=1
    else:
        a.pop(0)
        a.pop()
        cn+=1
    if len(a)==1:
        cn+=1
        break

print(cn)