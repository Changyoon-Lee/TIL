import sys
# sys.stdin = open('섹션 5/2. 쇠막대기/in1.txt')

a = input()
gyup = 0
zogak = 0
last = ''

for i in a:
    
    if last=='(':
        if i==')':
            zogak+=gyup
        else : gyup+=1

    else:
        if i==')':
            zogak+=1
            gyup-=1

    
    last = i
print(zogak+gyup)
