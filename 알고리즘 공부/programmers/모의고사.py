from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]


# 시간은 밑에꺼가 더 빠름

def que(q,a):
    cnt=0
    for i in a:
        temp = q.pop(0)
        if temp==i:
            cnt+=1
        q.append(temp)
    return cnt
def solution(answers):
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    
      
    answer = []
    max = 0
    for i, v in enumerate([a,b,c]):
        temp = que(v, answers)
        if temp>max:
            max=temp
            answer=[]
            answer.append(i+1)
        elif temp==max:
            answer.append(i+1)

    return answer