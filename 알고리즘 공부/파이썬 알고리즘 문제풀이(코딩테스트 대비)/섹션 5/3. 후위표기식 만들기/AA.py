import sys
# sys.stdin = open('섹션 5/3. 후위표기식 만들기/in1.txt')

a = list(map(str, input()))


stack = []
res = ''

for i in a:
    if i.isdecimal():
        res+=i

    else :
        if i == '(':
            stack.append(i)

        elif i == '*' or i == '/':
            while stack and stack[-1] not in ['+','-','(']:
                res+= stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(i)
        
        elif i == ')':
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res+=stack.pop()
print(res)