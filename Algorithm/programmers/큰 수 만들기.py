# 코딩테스트 연습 > 탐욕법(Greedy) > 큰 수 만들기

# DFS로 풀었을 때 런타임에러, 시간초과 발생
# def solution(number, k):
#     max_num=0
    
#     def DFS(i, res):
#         nonlocal number, k, max_num
#         if len(res)==len(number)-k+1:
#             if int(res)>max_num:
#                 max_num=int(res)
#             return
#         elif i<len(number):
#             DFS(i+1,res+number[i])
#             DFS(i+1,res)

#     DFS(0,'0')

#     return str(max_num)


def solution(number, k):
    number = list(map(int, str(number)))
    Q=[]
    
    for x in number:
        while k>0 and Q and Q[-1]<x:
            Q.pop()
            k-=1
        Q.append(x)
    if k!=0:
        return ''.join(map(str,Q[:-k]))
    return ''.join(map(str, Q))


print(solution("19", 1))

# 테스트 1 〉	통과 (0.04ms, 10.4MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.08ms, 10.4MB)
# 테스트 4 〉	통과 (0.37ms, 10.3MB)
# 테스트 5 〉	통과 (0.56ms, 10.4MB)
# 테스트 6 〉	통과 (5.39ms, 10.7MB)
# 테스트 7 〉	통과 (16.14ms, 13.7MB)
# 테스트 8 〉	통과 (32.46ms, 15.5MB)
# 테스트 9 〉	통과 (92.54ms, 37MB)
# 테스트 10 〉	통과 (155.80ms, 33.4MB)
# 테스트 11 〉	통과 (0.04ms, 10.4MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)