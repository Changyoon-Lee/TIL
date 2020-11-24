from itertools import permutations

def solution(numbers):
    cnt = 0
    num_list = set()
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            num_list.add(int(''.join(j)))
    
    # 소수 리스트 뽑기  
    # 조합으로 나온 가장큰수의 제곱근 이하의 소수에 대해서 나누어떨어지는지 여부만 확인하면 됨
    n=int(max(num_list)**(0.5)+1)
    print(n)
    ch = [0]*(n+1)
    prime_list=[]
    for i in range(2, n+1):
        if ch[i]==0:
            prime_list.append(i)
            for j in range(i, n+1, i):
                ch[j]=1    
    
    # 소수인지 체크 하여 카운트
    for i in num_list:
        if i<=prime_list[-1]:
            if i in prime_list:
                cnt+=1
        else :
            for j in prime_list:
                if i%j==0: break

            else : cnt+=1  
    
    return cnt

# 테스트 1 〉	통과 (0.09ms, 10.5MB)
# 테스트 2 〉	통과 (2.50ms, 10.5MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (1.18ms, 10.4MB)
# 테스트 5 〉	통과 (5.33ms, 10.4MB)
# 테스트 6 〉	통과 (0.05ms, 10.5MB)
# 테스트 7 〉	통과 (0.10ms, 10.5MB)
# 테스트 8 〉	통과 (5.19ms, 10.4MB)
# 테스트 9 〉	통과 (0.06ms, 10.4MB)
# 테스트 10 〉	통과 (3.61ms, 10.4MB)
# 테스트 11 〉	통과 (0.60ms, 10.5MB)
# 테스트 12 〉	통과 (0.31ms, 10.4MB)