def rotate_cw(l): # 시계방향 회전
    n = len(l)
    res=[[0]*n for _ in range(n)]

    for i in range(len(l)):
        for j in range(len(l[i])):
            res[j][n-1-i] = l[i][j]
    return res

def check(key,lock): # 일치하는지 여부 체크
    for row_k, row_l in zip(key,lock):
        for k, l in zip(row_k, row_l):
            if k+l != 1:
                return False
    else  : return True

def key_setting(key, n): # key움직이면서 lock이랑 사이즈 맞춰주기
    
    m = len(key)
    for x in range(m, -n+1,-1):
        for y in range(m, -n+1, -1):
            res=[[0]*n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    if 0<=x-1+i<m and 0<=y-1+j<m:
                        res[i][j]=key[x-1+i][y-1+j]
            yield res

def solution(key, lock):
    for padded_key in key_setting(key, len(lock)):
        for temp in range(4):
            if check(padded_key, lock):
                return True
            if temp==3:
                break
            padded_key=rotate_cw(padded_key)
    
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 정확성  테스트
# 테스트 1 〉	통과 (0.58ms, 10.3MB)
# 테스트 2 〉	통과 (0.41ms, 10.2MB)
# 테스트 3 〉	통과 (5.21ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.3MB)
# 테스트 5 〉	통과 (10.95ms, 10.4MB)
# 테스트 6 〉	통과 (32.57ms, 10.3MB)
# 테스트 7 〉	통과 (141.79ms, 10.3MB)
# 테스트 8 〉	통과 (93.83ms, 10.3MB)
# 테스트 9 〉	통과 (106.92ms, 10.2MB)
# 테스트 10 〉	통과 (264.73ms, 10.3MB)
# 테스트 11 〉	통과 (207.17ms, 10.3MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 테스트 13 〉	통과 (8.44ms, 10.3MB)
# 테스트 14 〉	통과 (1.84ms, 10.2MB)
# 테스트 15 〉	통과 (0.20ms, 10.4MB)
# 테스트 16 〉	통과 (11.03ms, 10.3MB)
# 테스트 17 〉	통과 (3.76ms, 10.4MB)
# 테스트 18 〉	통과 (52.39ms, 10.3MB)
# 테스트 19 〉	통과 (1.63ms, 10.4MB)
# 테스트 20 〉	통과 (77.33ms, 10.3MB)
# 테스트 21 〉	통과 (50.56ms, 10.3MB)
# 테스트 22 〉	통과 (11.56ms, 10.3MB)
# 테스트 23 〉	통과 (3.40ms, 10.3MB)
# 테스트 24 〉	통과 (5.12ms, 10.2MB)
# 테스트 25 〉	통과 (167.14ms, 10.4MB)
# 테스트 26 〉	통과 (125.97ms, 10.3MB)
# 테스트 27 〉	통과 (221.31ms, 10.2MB)
# 테스트 28 〉	통과 (27.75ms, 10.3MB)
# 테스트 29 〉	통과 (5.84ms, 10.3MB)
# 테스트 30 〉	통과 (22.85ms, 10.2MB)
# 테스트 31 〉	통과 (104.71ms, 10.3MB)
# 테스트 32 〉	통과 (157.52ms, 10.3MB)
# 테스트 33 〉	통과 (20.83ms, 10.3MB)
# 테스트 34 〉	통과 (0.80ms, 10.2MB)
# 테스트 35 〉	통과 (1.37ms, 10.3MB)
# 테스트 36 〉	통과 (2.70ms, 10.3MB)
# 테스트 37 〉	통과 (2.74ms, 10.3MB)
# 테스트 38 〉	통과 (1.59ms, 10.3MB)