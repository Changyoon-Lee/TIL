import sys
# sys.stdin = open('섹션 3/3. 카드 역배치/in1.txt')
num_list = list(range(1,21,1))

for i in range(10):
    a,b = map(int,input().split())
    num_list[a-1:b] = num_list[a-1:b][::-1]

print(' '.join(list(map(str,num_list))))