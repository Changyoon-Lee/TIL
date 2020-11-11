import sys

# sys.stdin = open("섹션 3/9. 봉우리/in1.txt")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cn = 0
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)
a.append([0] * n)

for i in range(len(a)):
    a[i].insert(0, 0)
    a[i].append(0)


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
            cn += 1

print(cn)

