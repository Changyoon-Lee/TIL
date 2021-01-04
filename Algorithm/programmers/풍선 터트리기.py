# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 풍선 터트리기

def solution(a):
    L_min=a[0]
    R_min=a[-1]
    res=set()
    for i in range(len(a)):
        if L_min>=a[i]:
            L_min=a[i]
            res.add(i)
        j = len(a)-i-1    
        if R_min>=a[j]:
            R_min=a[j]
            res.add(j)
    
    return len(res)

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))


# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.27ms, 10.1MB)
# 테스트 4 〉	통과 (18.01ms, 14.2MB)
# 테스트 5 〉	통과 (89.29ms, 31.8MB)
# 테스트 6 〉	통과 (132.45ms, 42.6MB)
# 테스트 7 〉	통과 (179.77ms, 53.5MB)
# 테스트 8 〉	통과 (178.63ms, 53.3MB)
# 테스트 9 〉	통과 (175.74ms, 53.4MB)
# 테스트 10 〉	통과 (177.17ms, 53.5MB)
# 테스트 11 〉	통과 (297.82ms, 123MB)
# 테스트 12 〉	통과 (287.42ms, 123MB)
# 테스트 13 〉	통과 (256.29ms, 88.9MB)
# 테스트 14 〉	통과 (295.21ms, 123MB)
# 테스트 15 〉	통과 (296.63ms, 123MB)