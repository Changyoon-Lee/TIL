def solution(n):
    zinbub=[]
    while n>3:
        n, temp = divmod(n,3)
        if temp==0:
            n=n-1
            temp=3
        zinbub.append(temp)
    zinbub.append(n)
    
    return ''.join(list(map(str, zinbub))).replace('3','4')[::-1]

print(solution(12))