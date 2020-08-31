import sys
# sys.stdin=open('섹션 2/3. k번째 큰 수/in1.txt','rt')
n, k = map(int, input().split())
list_a = list(map(int, input().split()))

sum_list=[]
for i in range(len(list_a)):
    if i < len(list_a)-2:
        for j in range(i+1,len(list_a)):
            for w in range(j+1,len(list_a)):
                sum_list.append(list_a[i]+list_a[j]+list_a[w])
a = list(set(sum_list))
a.sort()
print(a[-k])