# 코딩테스트 연습 > 동적계획법(Dynamic Programming) > N으로 표현
from itertools import product
def solution(N, number):
    what={}
    i=0
    while i<8:
        i+=1 # 요게 사용횟수 역할
        what[i]=[int(i*str(N))] # 기본적으로 들어가는 것 ex> 2 세번 : 222
        for j in range(1, i//2+1): # ex) 4번사용 된거는 1번,3번의 조합 or 2번 2번의 조합
            for k in product(what[j],what[i-j]):
                what[i]+=[k[0]+k[1], k[0]-k[1], k[0]-k[1], k[0]*k[1],k[0]//k[1],k[1]//k[0]] # 가능한 사칙연산 추가
        what[i]=list(filter(lambda x:x>0, list(set(what[i])))) # 중복값, 0이하 값 filter
        if number in what[i]: # 원하는 숫자 만들어졌으면 사용횟수 리턴
            return i
    
    return -1

print(solution(2, 11))

# 정확성  테스트
# 테스트 1 〉	통과 (0.75ms, 10.3MB)
# 테스트 2 〉	통과 (0.03ms, 10.3MB)
# 테스트 3 〉	통과 (0.05ms, 10.4MB)
# 테스트 4 〉	통과 (7.21ms, 11.8MB)
# 테스트 5 〉	통과 (5.80ms, 10.9MB)
# 테스트 6 〉	통과 (0.21ms, 10.3MB)
# 테스트 7 〉	통과 (0.19ms, 10.4MB)
# 테스트 8 〉	통과 (6.50ms, 11.8MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)