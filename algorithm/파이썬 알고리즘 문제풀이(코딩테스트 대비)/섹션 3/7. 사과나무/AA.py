import sys

# sys.stdin = open("섹션 3/7. 사과나무/in1.txt")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

sum_tree = 0
for i in range(n):
    for j in range(n):
        x = i - n // 2
        y = j - n // 2
        if abs(x) + abs(y) <= n // 2:
            sum_tree += a[i][j]

print(sum_tree)
