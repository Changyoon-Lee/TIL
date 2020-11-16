# 코딩테스트 연습 > 해시


def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: len(x)) # 글자길이 짧은 순으로 정렬
    print(phone_book)
    n = len(phone_book)

    for i in range(n):
        l = len(phone_book[i])
        for j in range(i + 1, n):
            if phone_book[i] == phone_book[j][:l]:
                return False
    return answer


print(solution(["119", "97674223", "1195524421"]))

# 효율성 테스트
# 테스트 1 〉	통과 (2.97ms, 11.1MB)
# 테스트 2 〉	통과 (2.94ms, 11.1MB)
