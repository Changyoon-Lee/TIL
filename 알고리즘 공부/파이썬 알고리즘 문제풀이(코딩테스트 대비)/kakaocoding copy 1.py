def solution(v):
    v = v.lower()
    Q=[]
    for i in v:
        if i.isalpha() or i.isdecimal():
            Q.append(i)
            continue
        elif i in ['-','_','.']:
            Q.append(i)
    
    v = ''.join(Q)
    Q=[]
    last=''
    for i in v:
        if last==i=='.':
            continue
        else:
            Q.append(i)
        last=i

    if len(Q)>0 and Q[0]=='.':
        Q.pop(0)
    if len(Q)>0 and Q[-1]=='.':
        Q.pop(-1)
    
    if len(Q)==0:
        Q.append('a')

    if len(Q)>=16:
        Q = Q[:15]
        if Q[-1]=='.':
            Q.pop(-1)
    if len(Q)<=2:
        while len(Q)<=2:
            Q.append(Q[-1])


    return print(''.join(Q))

a ='abcdefghijklmn.p'
solution(a)