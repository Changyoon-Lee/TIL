# 코딩테스트 연습 > 스택/큐
from math import ceil


def solution(progresses, speeds):
    answer = []
    res = []
    for i, j in zip(progresses, speeds):
        res.append(ceil((100 - i) / j))

    stack = []
    for i in range(len(res)):
        stack.append(res[i])
        if i < len(res) - 1 and stack[0] >= res[i + 1]:
            pass
        else:
            answer.append(len(stack))
            stack = []

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
