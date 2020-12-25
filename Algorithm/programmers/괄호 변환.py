# 코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT > 괄호 변환

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
#   4-3. ')'를 다시 붙입니다. 
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
#   4-5. 생성된 문자열을 반환합니다.

def solution(p):
    
    def devide(p):
        nonlocal TFdict, final
        
        TF_num=0

        seq = 0 # 순서 체크
        if not p:
            return

        for i in range(len(p)):
            TF_num += TFdict[p[i]]
            if TF_num<0:
                seq = 1
            if TF_num==0:
                u = p[:i+1]
                v = p[i+1:]
                
                if seq==0:
                    final+=u
                    devide(v)
                else:
                    changed = change(u)
                    i+=1
                    final+='('
                    devide(v)
                            
                    final = final + ')'+changed
                break
    
    def change(p):
        if len(p)==2:
            return ""
        
        else :
            changed=""
            for i in range(1, len(p)-1):
                if p[i]=='(':
                    changed+=')'
                else:
                    changed+='('
            return changed

    TFdict={'(':1, ')':-1}
    final=""
    devide(p)

    return final

print(solution('()))((()()))((()'))


# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.01ms, 10.4MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.4MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.3MB)
# 테스트 11 〉	통과 (0.03ms, 10.2MB)
# 테스트 12 〉	통과 (0.04ms, 10.4MB)
# 테스트 13 〉	통과 (0.05ms, 10.3MB)
# 테스트 14 〉	통과 (0.07ms, 10.2MB)
# 테스트 15 〉	통과 (0.09ms, 10.2MB)
# 테스트 16 〉	통과 (0.22ms, 10.2MB)
# 테스트 17 〉	통과 (0.17ms, 10.2MB)
# 테스트 18 〉	통과 (0.24ms, 10.1MB)
# 테스트 19 〉	통과 (0.42ms, 10.3MB)
# 테스트 20 〉	통과 (0.31ms, 10.3MB)
# 테스트 21 〉	통과 (0.34ms, 10.2MB)
# 테스트 22 〉	통과 (0.17ms, 10.3MB)
# 테스트 23 〉	통과 (0.28ms, 10.3MB)
# 테스트 24 〉	통과 (0.08ms, 10.3MB)
# 테스트 25 〉	통과 (0.16ms, 10.2MB)