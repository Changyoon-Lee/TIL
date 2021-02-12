#!/bin/python3

import math
import os
import random
import re
import sys

n = 10 # num max_len : 자리수 10자리 제한
t = 10**n
# Complete the extraLongFactorials function below.
# 자리수 10^15 단위로 끊기
def big_int(n): # 자료형 형태 [~~, ~~]
    if n >= t:
        return list(divmod(n,t)) # [int(str(n)[:-10]), int(str(n)[-10:])]
        # 처음에 자리수 제한 15로 함 -> divmod(101761881188650584, 10e+15) => (10.0, 1761881188650592.0) 
        # 계산 오류나는데 자료형 overflow/underflow되는듯 -> 
        # int 표현범위 -2147483648~2147483647 -> 10자리로 제한하니까 됨
    else : return [n]
def big_int_multiply(n, m):# m은 big_int자료형,  n은 100이하의 숫자라고 설정하겠음
    res_list = [] # 각 자리수 리스트에 곱
    for i in range(len(m)):
        res_list.append(big_int(n*m[i]))
    for i in range(len(res_list)):
        if i ==0:
            res = res_list[i]
        else :
            if len(res_list[i])==2:
                res[-1]+=res_list[i][0]
                res.append(res_list[i][1])
            else : res.append(res_list[i][0])
    return res # res자료형태는 big_int형태
             
def Factorials(n):
    if n ==1 :
        return [1]
    else : 
        return big_int_multiply(n, Factorials(n-1))
     #16자리
def extraLongFactorials(n):
    res = Factorials(n)
    for i in range(len(res)):
        if i == 0:
            answer = str(res[i])
        else :
            
            answer += (10-len(str(res[i])))*'0'+str(res[i])
    return answer
if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
# 119622220865 480194561963161 495657715064383 733760000000000