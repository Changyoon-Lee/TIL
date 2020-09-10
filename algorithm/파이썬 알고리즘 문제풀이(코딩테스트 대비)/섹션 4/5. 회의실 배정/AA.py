import sys
sys.stdin = open('섹션 4/5. 회의실 배정/in1.txt')
n = int(input())
a = [0]*10
for _ in range(n):
    i, j = map(int, input().split())
    a[i:j]