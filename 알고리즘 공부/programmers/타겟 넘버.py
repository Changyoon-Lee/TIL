def solution(numbers, target):
    global cnt
    cnt = 0
    def DFS(i, sum):
        global cnt
        if i==len(numbers):
            if sum==target:
                cnt=cnt+1
        else:    
            DFS(i+1, sum+numbers[i])
            DFS(i+1, sum-numbers[i])
    DFS(0,0)
    return cnt

# nonlocal 하면 global 안쓰고 간단해 질 
print(solution([1, 1, 1, 1, 1],3))
