def solution(citations):
    res=0
    citations.sort(reverse=True)
    if citations[-1]>=len(citations):
        res = len(citations)
        return res
    else : 
        for i in range(1,len(citations)):
            if citations[i-1]>=i and citations[i]<=i:
                res = i
                break
        return res
    
    

print(solution([0,0,0]))