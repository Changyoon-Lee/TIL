import sys
# sys.stdin = open('섹션 4/7. 창고 정리/in1.txt')

n = int(input())

num_list = list(map(int,input().split()))

m = int(input())
for i in range(m):
    num_list.sort()
    num_list[0]+=1
    num_list[-1]-=1
print(max(num_list)-min(num_list))