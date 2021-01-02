# 코딩테스트 연습 > 깊이/너비 우선 탐색(DFS/BFS) > 단어변환

import copy

def word_diff(a,b):
    cnt=0
    for i,j in zip(a,b):
        if i!=j:
            cnt+=1
            if cnt==2:
                return 0
    return cnt



def solution(begin, target, words):
    res = []
    def DFS(mid, target, words, n):
        nonlocal res
        if target==mid:
            res.append(n)
            return
        else :
            for i in words:
                temp_words=copy.deepcopy(words)
                if word_diff(mid,i)==1:
                    temp_words.remove(i)
                    DFS(i, target, temp_words, n+1)

        return 0


    begin = list(map(str, begin))
    target = list(map(str, target))
    words = [list(map(str, i)) for i in words]
    
    answer = DFS(begin, target, words, 0)
    if res:
        return min(res)

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.3MB)
# 테스트 2 〉	통과 (7.31ms, 10.4MB)
# 테스트 3 〉	통과 (77.39ms, 10.4MB)
# 테스트 4 〉	통과 (0.15ms, 10.4MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)