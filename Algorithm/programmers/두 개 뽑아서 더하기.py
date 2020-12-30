from itertools import combinations

def solution(numbers):
    res = [sum(i) for i in combinations(numbers,2)]
    res = list(set(res))
    res.sort()
    return res

print(solution([2,1,3,4,1]))