from itertools import cycle
def solution(numbers):
    numbers=list(map(str, numbers))
    numbers = sorted(numbers, key=lambda num:''.join([j for _,j in zip(range(5),cycle(num))]), reverse=True)

    return str(int(''.join(numbers)))
    


print(solution([6, 10, 2]))