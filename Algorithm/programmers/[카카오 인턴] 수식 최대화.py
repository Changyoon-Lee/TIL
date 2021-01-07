# 2020 카카오 인턴십
from copy import deepcopy
from collections import deque, defaultdict


def solution(expression):
    def cal(symbol, a, b):
        if symbol=='+':
            return a+b
        elif symbol=='-':
            return a-b
        else:
            return a*b

    def devide(expression):
        nonlocal num_ori, fig_dic_ori
        for i in range(len(expression)):
            if not expression[i].isdecimal():
                fig_dic_ori[expression[i]]+=1
                num_ori.append(int(expression[:i]))
                num_ori.append(expression[i])
                devide(expression[i+1:])
                break
        else:
            num_ori.append(int(expression))
            num_ori.append('last')
    
    turn=[['+','-','*'], ['+','*','-'],['-','+','*'],['-','*','+'],['*','+','-',],['*','-','+']]
    max_res=0
    fig_dic_ori=defaultdict(int)
    num_ori=[]
    devide(expression)
    for symbols in turn:
        Q=deque(num_ori)
        fig_dic=deepcopy(fig_dic_ori)
        for symbol in symbols:
            while fig_dic[symbol] or Q[-1]!='last':
                fig = Q.popleft()
                if fig==symbol:
                    fig_dic[symbol]-=1
                    Q.append(cal(fig, Q.pop(), Q.popleft()))
                else:
                    Q.append(fig)

        if max_res<abs(Q[0]):
            max_res=abs(Q[0])


    return max_res


import re
from itertools import permutations

def solution2(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)

    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])

    #3
    return max(abs(int(x)) for x in a)
print(solution2('2-990-5+2'))




