import sys
sys.stdin = open('섹션 4/2. 랜선자르기/in5.txt')

n, k = map(int, input().split())

num_list = [int(input()) for _ in range(n)]

upper = max(num_list)
search = upper//2
lower = 0

while True:
    cnt=0
    for num in num_list:
        cnt += num//search

    if cnt < k:
        upper = search
        search = (search + lower)//2

    else :
        lower = search
        search = (search + upper)//2
    
    if search==lower or search==upper:
        print(search)
        break
