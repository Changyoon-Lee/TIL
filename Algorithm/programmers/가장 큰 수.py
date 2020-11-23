# 코딩테스트 연습 > 정렬 > 가장 큰 수

from itertools import cycle
def solution(numbers):
    numbers=list(map(str, numbers))
    numbers = sorted(numbers, key=lambda num:''.join([j for _,j in zip(range(5),cycle(num))]), reverse=True)

    return str(int(''.join(numbers)))
    
# 최대 5자리 수 이므로 itertools cycle을 이용해 모두 5자리일때를 기준으로 정렬
# 문자인 숫자도 앞자리 크기 순으로 정렬된다

print(solution([6, 10, 2]))

# 테스트 1 〉	통과 (846.26ms, 23.8MB)
# 테스트 2 〉	통과 (275.01ms, 17.4MB)
# 테스트 3 〉	통과 (1413.30ms, 28MB)