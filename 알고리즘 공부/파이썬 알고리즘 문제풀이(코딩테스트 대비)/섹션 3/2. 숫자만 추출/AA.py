import sys
# sys.stdin = open('섹션 3/2. 숫자만 추출/in1.txt')
a = input()
num = ''
for i in a:
    try:
        num = num+str(int(i))
    except : pass
num = int(num)
print(num)
n=1
for i in range(1,num//2+1):
    if num%i==0:
        n+=1
print(n)
