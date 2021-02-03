def solution(routes):
    routes.sort(key=lambda x:x[1])
    cnt=0
    for i in range(len(routes)):
        if i==0:
            bar = routes[i][1]
            cnt+=1
            continue

        if routes[i][0]<=bar:
            continue
        else :
            cnt+=1
            bar = routes[i][1] 
    return cnt

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))