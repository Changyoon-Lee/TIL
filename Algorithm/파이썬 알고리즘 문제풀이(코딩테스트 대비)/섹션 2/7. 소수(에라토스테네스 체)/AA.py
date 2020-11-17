import sys
sys.stdin = open('7. 소수(에라토스테네스 체)/in5.txt','rt')

# n = int(input())
n=100000
# num_list=list(range(2,n+1))


# for i in num_list:
#     for j in range(2*i, n+1,i):
#         try:
#             num_list.remove(j)
#         except:pass

# print(len(num_list))

ch=[0]*(n+1)
cnt=0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)