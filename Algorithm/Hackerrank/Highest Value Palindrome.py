#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
    # 대칭 아닌거 일단 탐색하기
    # 비대칭 부분 고칠 거 체크
    # k 남으면 앞자리 부터 9로 만들어주기
    # 고칠게 k 보다 크면 -1 return
def highestValuePalindrome(s, n, k):
    s = list(map(str,s))
    not_9=[]
    cnt = 0
    for i in range(int(len(s)/2)):
        
        if s[i]!=s[n-1-i]: # 대칭아닐떄
            if s[i]!='9' and s[n-1-i]!='9': # 둘중에하나 9 아닐때
                not_9.append([i,1])
                cnt+=1
            else : # 
                # idx_9notsym.append(i)
                k -= 1
                s[i]=s[n-1-i]='9'
                
                
        
        elif s[i]!='9': # 대칭인대 9 아닐때
            not_9.append([i,0])
    
    
    if cnt>k:
        return '-1'
    for i in range(len(not_9)):
        if not_9[i][1]==0:
            if k-cnt>=2:
                k-=2
                s[not_9[i][0]]=s[n-1-not_9[i][0]]='9' 
        else :
            if k-cnt>=1:
                s[not_9[i][0]]=s[n-1-not_9[i][0]]='9'
                k -= 2
                cnt -=1
            else:
                k -= 1
                s[not_9[i][0]]=s[n-1-not_9[i][0]]=str(max(int(s[not_9[i][0]]), int(s[n-1-not_9[i][0]])))
                
    if len(s)%2!=0:
        if s[len(s)//2]!='9' and k>0:
            s[len(s)//2]='9'
    return ''.join(s)
        # 
        # 
        # 
print(highestValuePalindrome('9994999', 7, 1))