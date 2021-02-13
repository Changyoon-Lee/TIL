# S의 subset의 원소 두개를 합한것이 k 로 나누어 떨어지지 않는다
import math
from collections import defaultdict
def nonDivisibleSubset(k, s):
    remainder_dic = defaultdict(int)

    for i in s:
        remainder_dic[i%k] += 1

    # dict에서 1 이랑 k-1 중에 큰거
    # 홀수 [1 or k-1, 2 or k-2, ... k//2 or k//2+1]
    # 짝수 [ , , ... k//2 -1]
    res = 0
    for i in range(1, math.ceil(k/2)):
        res += max(remainder_dic[i], remainder_dic[k-i])
    if remainder_dic[0]!=0: # 나누어떨어지는 것들이 있으면 하나 추가
        res+=1
    if k%2==0 and remainder_dic[k/2]!=0: # 짝수일때 나머지가 k/2 인값이 있으면 하나 추가 
        res+=1

    return res
    # Write your code here