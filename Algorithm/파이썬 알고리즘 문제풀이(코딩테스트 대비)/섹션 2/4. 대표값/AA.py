import sys
# sys.stdin=open('섹션 2/4. 대표값/in1.txt','rt')
n = int(input())
score = list(map(int, input().split()))

ave = round(sum(score)/n)

score_v = [(i+1,abs(val-ave),val) for i, val in enumerate(score)]
b = sorted(score_v, key=lambda x : (x[1],x[0]))
print(int(ave), b[0][0])