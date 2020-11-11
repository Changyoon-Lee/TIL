import sys

# sys.stdin = open("섹션 3/8. 곳감/in4.txt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
gam = 0

for _ in range(m):
    index, direc, num = map(int, input().split())
    num = num%n
    index -= 1
    if direc ==0:
        a[index] = a[index][num:] + a[index][:num]

    else:
        a[index] = a[index][-num:] + a[index][:-num]


s, e = 0, n

for i in range(n):
    for j in range(s, e):
        gam += a[i][j]

    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(gam)