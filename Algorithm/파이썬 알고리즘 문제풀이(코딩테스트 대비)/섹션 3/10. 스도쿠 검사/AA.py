import sys

# sys.stdin = open("섹션 3/10. 스도쿠 검사/in2.txt")

a = [list(map(int, input().split())) for _ in range(9)]

try:
    for i in range(0, 9, 3):
        chk_sero = []

        for j in range(0, 9, 3):
            chk_sq = []
            for k in range(3):
                if len(list(set(a[i + k]))) != 9:

                    raise NotImplementedError
                chk_sero += [a[j + k][i]]
                chk_sq += a[i+k][j: j+3]

            if len(list(set(chk_sq))) != 9:
                raise NotImplementedError

        if len(list(set(chk_sero))) != 9:
            raise NotImplementedError
    else:
        print("YES")
except:
    print("NO")
