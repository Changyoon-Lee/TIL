import sys
# sys.stdin = open('섹션 4/9. 증가수열 만들기/in1.txt')

n = int(input())

a = list(map(int, input().split()))
n_list = ''

last_num = 0
while a:
    if a[0]>last_num and a[-1]>last_num:
        if a[0]<a[-1]:

            n_list+='L'
            last_num = a.pop(0)
        else :
            n_list+='R'
            last_num = a.pop(-1)
    elif a[0]>last_num:
        n_list+='L'
        last_num = a.pop(0)
    elif a[-1]>last_num:
        n_list+='R'
        last_num = a.pop(-1)
    else : break


print(len(n_list),"\n"+n_list)