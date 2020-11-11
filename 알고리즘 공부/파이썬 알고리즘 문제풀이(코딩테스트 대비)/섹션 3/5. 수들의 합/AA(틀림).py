import sys

# sys.stdin = open("섹션 3/5. 수들의 합/in1.txt")

m, n = map(int, input().split())

nums = list(map(int, input().split()))
cn = 0
for i in range(m):
    for j in range(i + 1, m):
        if sum(nums[i:j]) == n:
            cn += 1
            break
        elif sum(nums[i:j]) > n:
            break

print(cn)
