# 코딩테스트 연습 > 스택/큐 > 주식가격

def solution(prices):
    res=[]
    for i in range(len(prices)):
        cnt=0
        for j in range(i+1, len(prices)):
            cnt+=1
            if prices[j]>=prices[i]:
                continue
            else:break
        res.append(cnt)
            
    return res

print(solution([1, 2, 3, 2, 3]))

# 효율성  테스트
# 테스트 1 〉	통과 (124.54ms, 18.8MB)
# 테스트 2 〉	통과 (92.77ms, 17.6MB)
# 테스트 3 〉	통과 (146.64ms, 19.6MB)
# 테스트 4 〉	통과 (105.34ms, 18.3MB)
# 테스트 5 〉	통과 (75.33ms, 17.1MB)