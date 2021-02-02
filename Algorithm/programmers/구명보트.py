import math

def solution(people, limit):
    people.sort(reverse=True)
    cnt=0
    lt=0
    rt=len(people)-1

    while people[lt]>limit/2:
        if lt==rt:
            cnt+=1
            return cnt
        
        if people[lt] + people[rt]<=limit:
            lt+=1
            rt-=1
            cnt+=1
        
        else :
            lt+=1
            cnt+=1           

    
    cnt+= math.ceil((rt-lt+1)/2)
    return cnt

print(solution([70, 50, 50,40,40,40]	, 110))