import heapq
from operator import itemgetter

def solution(jobs):
    time=0
    t=0
    jobs.sort(key=lambda x: x[1])
    n  = len(jobs)
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= t:
                t+=jobs[i][1]
                time += t-jobs[i][0]
                del jobs[i]
                break
            elif i == len(jobs)-1:
                t +=1
    return time//n

def solution2(job):
    cur = 0   # 현재 시점
    jobs = sorted(job.copy(), key=lambda x:x[1])
    time = 0
    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= cur:
                cur += jobs[i][1]
                time += (cur-jobs[i][0])
                del jobs[i]
                break
            elif i == len(jobs)-1:
                cur += 1
    return time//len(job)

print(solution([[0, 1], [2, 5], [3, 5], [4, 4]]))