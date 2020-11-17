import sys
# sys.stdin = open('6. 자릿수의 합/in1.txt','rt')
n = int(input())
num = list(map(int, input().split()))

def digit_sum(x):
    x_sum=0
    for i in range(len(str(x))):
        x_sum+=int(str(x)[i])
    return x_sum
max_n_idx=0
max_n=0
for i, n in enumerate(num):
    if max_n<digit_sum(n):
        max_n=digit_sum(n)
        max_n_idx=i
print(num[max_n_idx])

    