# 코딩테스트 연습 > Summer/Winter Coding(2019) > 멀쩡한 사각형

from math import gcd

def solution(w,h):
    num = gcd(w,h)
    
    answer = w*h - num*(w/num+h/num-1)
    return answer