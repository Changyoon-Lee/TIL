def solution(gems):
    lenth=len(gems)
    n = len(set(gems))
    li=ri=0
    ran = len(gems)
    res=[1,1]
    tempset=set()
    while ran+1!=n and ri!=lenth-1:
        
        while ri<=li+ran:
            tempset.add(gems[ri])
            if len(tempset)==n:
                
                break
            ri+=1
        
        while len(tempset)==n :
            if gems[li] in gems[li+1:ri]:
                li+=1
            else :
                ran=ri-li
                res=[li+1,ri+1]
                tempset.remove(gems[li])
                li+=1
    return res

print(solution(["AA", "AB", "AC", "AA", "AC"]))