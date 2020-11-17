answer=[]
sets=[]
menudic={}

def DFS(a, n, j ,course):#(level, 'ABCDE', 만들메뉴조합)
    global sets

    if len(j)>max(course):
        return
    if a==len(n):
        if len(j) in course:
            sets.append(j)
        return
        
    else:
        DFS(a+1,n, j+n[a],course)
        DFS(a+1,n, j,course)

def solution(orders,course):
    global sets,menudic,answer
    
    for i in orders:
        li = list(map(str, i))
        li.sort()
        i = ''.join(li)

        DFS(0, i, '', course)

        for k in sets:
            menudic[k]=menudic.get(k, 0)+1

        sets=[]



    
    for i in course:
        maxval=0
        for key, value in menudic.items():        
            if len(key)==i:
                if value>maxval:
                    maxval=value
            
        for key, value in menudic.items():        
            if len(key)==i and value==maxval and value>=2:
                answer.append(key)

                
    answer.sort()
    return print(answer)

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])