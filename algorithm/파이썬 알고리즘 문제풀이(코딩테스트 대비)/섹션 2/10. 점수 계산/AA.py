import sys
# sys.stdin = open('섹션 2/10. 점수 계산/in1.txt')

n = int(input())
num_list = list(map(int, input().split()))
cnt=1
score=0
for i in num_list:
    if i==1:
        score+=cnt
        cnt+=1

    else:
        cnt=1

print(score)