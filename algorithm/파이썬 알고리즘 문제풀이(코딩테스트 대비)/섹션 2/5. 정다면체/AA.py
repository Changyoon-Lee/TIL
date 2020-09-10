import sys
# sys.stdin=open('5. 정다면체/in1.txt','rt')

n, m = map(int,input().split())
sum_list=[]
for i in range(1,n+1):
    for j in range(1,m+1):
        sum_list.append(i+j)

num=[]
k=0
for i, a in enumerate(list(set(sum_list))):
    
    if i==0:
        num.append(a)

    else :
        if k==sum_list.count(a):
            num.append(a)
        elif k<sum_list.count(a):
            num=[]
            num.append(a)
            k = sum_list.count(a)
        else : continue

for i in num:
    print(i, end=' ')