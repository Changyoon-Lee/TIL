import sys
# sys.stdin = open('섹션 2/9. 주사위 게임/in1.txt')

n = int(input())
score_list=[]

for i in range(n):
    nums = list(map(int, input().split()))
    temp = []
    for n in set(nums):
        if nums.count(n)==3:
            score = 10000+n*1000

        if nums.count(n)==2:
            score = 1000+n*100

        if nums.count(n)==1:
            temp.append(n)
            if len(temp) == 3:
                score = max(temp)*100

    score_list.append(score)

print(max(score_list))