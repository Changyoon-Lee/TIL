import heapq
from operator import itemgetter

def solution(jobs):
    hq=[]
    time=[]
    t=0
    delay=0
    jobs.sort(key=itemgetter(0,1))

    for i in jobs:
        if i[0]<=t:
            heapq.heappush(hq, i[1])
        else:
            while not hq:
                t+=heapq.heappop(hq)
                time.append(t)
            


        if :
            if i[0]>t:
                t=i[0]+i[1]
                time.append(t)
            else :
                t+=i[1]
                time.append(t)
        delay+=i[0]
    size = len(hq)
    for i in range(size):
        t+=heapq.heappop(hq)
        time.append(t)

    return (sum(time)-delay)//len(jobs)

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