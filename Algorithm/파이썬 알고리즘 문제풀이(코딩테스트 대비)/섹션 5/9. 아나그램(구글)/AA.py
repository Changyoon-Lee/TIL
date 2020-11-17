import sys
# sys.stdin = open('섹션 5/9. 아나그램(구글)/in1.txt')

a=input()
b=input()
str1={}
str2={}

for i, j in zip(a, b):
    str1[i] = str1.get(i,0)+1
    str2[j] = str2.get(j,0)+1

if str1==str2:
    print('YES')
else : 
    print('NO')