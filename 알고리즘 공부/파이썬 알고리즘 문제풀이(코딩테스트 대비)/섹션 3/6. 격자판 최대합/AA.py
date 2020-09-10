import sys

# sys.stdin = open('섹션 3/6. 격자판 최대합/in3.txt')

num_list = []
max_list = 0
dagak1 = 0
dagak2 = 0
sero = 0
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))
    num_list.append(a)

for i in range(n):
    sero = 0
    if max_list < sum(num_list[i]):
        max_list = sum(num_list[i])
    for j in range(n):
        sero += num_list[j][i]
    if max_list < sero:
        max_list = sero

    dagak1 += num_list[i][i]
    dagak2 += num_list[i][n-i-1]
print(max(max_list, dagak1, dagak2))
