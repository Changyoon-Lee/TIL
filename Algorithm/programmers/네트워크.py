# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 네트워크


from collections import deque

def solution(n, computers):
    chk = [0]*n
    q = deque() # 연결된 인덱스 저장
    cnt = 0
    for i in range(len(computers)):
        if chk[i]==0: # chk 안된거면 다음을 진행 
            chk[i]=1
            q.append(i) # chk에서 체크했던건지 보고 q에 넣음
            while q:
                idx = q.popleft()
                for j in range(len(computers[idx])):
                     # q 에서 꺼낸 인덱스에해당하는 컴퓨터의 리스트를 돌면서 연결되어있고 chk안한거면 q에 집어넣음
                    if computers[idx][j]==1 and chk[j]==0:
                        chk[j]=1
                        q.append(j)
                        
            cnt+=1
                
        
    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.05ms, 10.2MB)
# 테스트 4 〉	통과 (0.05ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.24ms, 10.1MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.11ms, 10.2MB)
# 테스트 9 〉	통과 (0.10ms, 10.2MB)
# 테스트 10 〉	통과 (0.11ms, 10.2MB)
# 테스트 11 〉	통과 (0.97ms, 10.4MB)
# 테스트 12 〉	통과 (1.11ms, 10.2MB)
# 테스트 13 〉	통과 (0.31ms, 10.2MB)