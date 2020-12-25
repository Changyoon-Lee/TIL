# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 삼각 달팽이

def solution(n):
    semo = [[0]*i for i in range(1,n+1)]
    i=1
    a=b=c=0
    while i<=n*(n+1)/2: # 
        if semo[a][b]!=0: # 만약 그자리에 0이 아닌것이 있으면 index변경
            c+=1
            a+=2
            b+=1
        semo[a][b]=i

        if b==c and a<n-1-c:# down
            a+=1
        elif a==n-c-1 and a-c!=b: #right
            b+=1

        else: # up
            a-=1
            b-=1
    

        i+=1
    return sum(semo, [])

print(solution(8))

# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (2.40ms, 10.8MB)
# 테스트 5 〉	통과 (2.11ms, 10.9MB)
# 테스트 6 〉	통과 (2.26ms, 10.8MB)
# 테스트 7 〉	통과 (1368.91ms, 57MB)
# 테스트 8 〉	통과 (1313.60ms, 57.7MB)
# 테스트 9 〉	통과 (1077.69ms, 58.6MB)