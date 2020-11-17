import sys
# sys.stdin = open('섹션 5/1. 가장 큰 수/in1.txt')

num, n = input().split()
num = [int(i) for i in num]
n = len(num)-int(n)
def ma(a):
    k=0
    for i in a:
        if i>k:
            k=i
    a.index(k)
    return k, a.index(k)


idx=0
m=n
maxnum=''
for i in range(n):
    k, temp_idx = ma(num[idx:-m]+[num[-m]])
    idx = idx+ temp_idx +1
    maxnum+=str(k)
    m-=1


print(maxnum)
