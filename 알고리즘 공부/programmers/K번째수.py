import heapq

def solution(array, commands):
    answer = []
    
    for i in commands:
        temp = array[i[0]-1:i[1]]
        heapq.heapify(temp)
        for _ in range(i[2]):
            a = heapq.heappop(temp)
        answer.append(a)
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))