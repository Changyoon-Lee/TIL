def climbingLeaderboard(ranked, player):
    #먼저 중복제거한 리스트를 만든다
    last=0
    num=[]
    for i in ranked:
        if i!=last:
            num.append(i)
        last=i
    
    #player점수가 정렬되어있으므로 ri를 움직이면서 체크
    res = []
    rank=len(num)
    ri=len(num)-1
    for num_p in player:
        while True:
            if num[ri]>num_p:
               rank=ri+1+1
               break
            else :
                ri-=1
                if ri<0:
                    rank=1
                    break 
        res.append(rank)
    return res

print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
