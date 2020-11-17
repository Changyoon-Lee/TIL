# 각 심사원이 몇명을 담당할지
def solution(n, times):
    n*times[0]
    board = [0] * len(times)
    lt=0
    rt=n*times[0]
    max_time=(lt+rt)//2
    while lt!=rt:
        num=0
        
        for i in times:
            num += max_time//i
        if num>=n:
            rt = max_time
            max_time=(lt+rt)//2
        else:
            lt = max_time+1
            max_time=(lt+rt)//2
        
    return max_time