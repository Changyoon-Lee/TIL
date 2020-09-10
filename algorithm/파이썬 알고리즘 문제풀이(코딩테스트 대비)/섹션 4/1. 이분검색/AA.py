import sys
sys.stdin = open('섹션 4/1. 이분검색/in5.txt','rt')

n, num = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()
idx=n//2
lower =0
upper = n
while True:
    if num < num_list[idx]:
        upper = idx
        idx = idx//2
    elif num > num_list[idx]:
        lower = idx
        idx = idx+(upper-lower)//2
    else : print(idx+1); break