import sys
# sys.stdin = open('섹션 5/4. 후위식 연산/in1.txt')

a = input()
res = 0
stack = []
for i in a:
    if i.isdecimal():
        stack.append(int(i))
    else :
        x2=stack.pop()
        x1=stack.pop()
        if i =='*':
            stack.append(x1*x2)
        elif i =='/':
            stack.append(x1/x2)
        elif i =='+':
            stack.append(x1+x2)
        elif i =='-':
            stack.append(x1-x2)
print(stack[0])