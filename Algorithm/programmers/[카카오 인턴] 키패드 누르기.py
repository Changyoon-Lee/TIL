def solution(numbers, hand):
    num_dic=dict()
    for i in range(1,10):
        num_dic[str(i)]=((i-1)//3,(i-1)%3)
    num_dic['*']=(3, 0)
    num_dic['0']=(3, 1)
    num_dic['#']=(3, 2)

    res=''
    last=dict()
    last['L']=(3,0)
    last['R']=(3,2)
    for i in numbers:
        if i in [1,4,7]:
            res+='L'
            last['L']=num_dic[str(i)]
        elif i in [3,6,9]:
            res+='R'
            last['R']=num_dic[str(i)]
        else:
            L_dis=0
            R_dis=0
            for a,b,c in zip(num_dic[str(i)],last['L'],last['R']):
                L_dis+=abs(a-b)
                R_dis+=abs(a-c)
            if L_dis>R_dis:
                res+='R'
                last['R']=num_dic[str(i)]
            elif L_dis<R_dis:
                res+='L'
                last['L']=num_dic[str(i)]
            else :
                temp = hand[0].upper()
                res+=temp
                last[temp]=num_dic[str(i)]


    return res

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],'left'))

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.02ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (0.03ms, 10.3MB)
# 테스트 11 〉	통과 (0.06ms, 10.3MB)
# 테스트 12 〉	통과 (0.05ms, 10.4MB)
# 테스트 13 〉	통과 (0.12ms, 10.2MB)
# 테스트 14 〉	통과 (0.22ms, 10.3MB)
# 테스트 15 〉	통과 (0.72ms, 10.3MB)
# 테스트 16 〉	통과 (0.53ms, 10.3MB)
# 테스트 17 〉	통과 (1.14ms, 10.3MB)
# 테스트 18 〉	통과 (1.12ms, 10.4MB)
# 테스트 19 〉	통과 (1.14ms, 10.3MB)
# 테스트 20 〉	통과 (1.22ms, 10.3MB)