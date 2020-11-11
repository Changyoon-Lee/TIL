


info =["java backend junior pizza 150","python frontend senior chicken 210",
"python frontend senior chicken 150","cpp backend senior pizza 260",
"java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"]
def solution(info, query):
    answer=[]
    Qori=[]
    for i in info:
        Qori.append(list(i.split()))
    
    query = [' '.join(list(i.split(' and '))).split() for i in query]
    for q in query:
        Q=Qori[:]
        cnt=0
        for i,val in enumerate(q):
            size = len(Q)
            
            if 0<=i<=3 and val=='-':#쿼리의 val이 -이면 통과
                continue

            elif 0<=i<=3 : #쿼리값이 있으면 필터링
                for _ in range(size):
                               
                    ch = Q.pop(0)
                    if ch[i]==val:
                        Q.append(ch)
            if i==4:
                for _ in range(size):
                    ch = Q.pop(0)
                    if int(ch[i])>=int(val):
                        Q.append(ch)
        answer.append(len(Q))

    return answer

solution(info, query)
