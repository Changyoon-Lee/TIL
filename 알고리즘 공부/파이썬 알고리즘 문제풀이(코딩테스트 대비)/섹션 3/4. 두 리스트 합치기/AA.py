import sys
# sys.stdin = open('섹션 3/4. 두 리스트 합치기/in1.txt')

n = input()
n_list = list(map(int,input().split()))
m = input()
m_list = list(map(int,input().split()))
n_list.extend(m_list)
n_list.sort()
a = ' '.join(list(map(str,n_list)))
print(a)


