import sys
# sys.stdin = open('섹션 2/8. 뒤집은 소수/in3.txt')

def isPrime(x):
    if x>=2:
        for i in range(2, x//2+1):
            if x%i==0:
                return False
        return True
    else :return False
def reverse(x):
    backnum = int(x[::-1])
    return backnum

primelist=[]
N = int(input())
nums = list(map(str, input().split()))

for i in nums:
    if isPrime(reverse(i)):
        primelist.append(reverse(i))

for i in primelist:
    print(i,end=' ')


