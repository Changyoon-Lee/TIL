import sys
sys.stdin = open('섹션 6/1. 재귀함수란(이진수출력)/in1.txt','rb')

n = int(input())
a=''
def zinsu(n):

    if n:
        zinsu(n//2)
        print(n%2, end='')
    else:return    
zinsu(n)