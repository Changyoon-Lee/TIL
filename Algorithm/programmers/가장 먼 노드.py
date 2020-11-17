from collections import defaultdict

def solution(n, edge):
    node=defaultdict(set)
    for i in edge:
        node[i[0]].add(i[1])
        node[i[1]].add(i[0])
    
    Q = [(0,1)]
    out = set([1])
    cnt=0
    while Q:
        size = len(Q)
        cnt += 1
        res = len(set(Q))
        for _ in range(size):
            num = Q.pop(0)[1]
            
            for i in node[num]:
                if i not in out:
                    Q.append((cnt, i))
                    out.add(i)
        
    return res

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))