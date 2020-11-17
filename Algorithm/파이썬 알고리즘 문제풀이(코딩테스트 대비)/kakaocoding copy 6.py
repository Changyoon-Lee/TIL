def solution(board, r, c):
    ch = [[0]*4 for _ in range(4)]
    ch1 = [[0]*4 for _ in range(4)]
    dx=[-1,0,1,0,-2,0,2,0]
    dy=[0,1,0,-1,0,2,0,-2]
    last=0
    Q=[]
    Q.append((r,c))
    while sum(sum(board,[]))!=0:
        tmp=Q.pop(0)
        cnt=0
        for i in range(8):
            x = tmp[0]+dx[i]
            y = tmp[1]+dy[i]
            if abs(dx[i])==1 or abs(dy[i])==1:
                if 0<=x<=3 and 0<=y<=3 and ch[x][y]<15:
                    ch[x][y] += 1#갔던길 반복적으로 안가기위함
                    ch1[x][y] = ch1[tmp[0]][tmp[1]]+1
                    Q.append((x,y))
                    if last!=0 and board[x][y]==last:
                        Q=[]
                        Q.append((x,y))
                        board[x][y]=0
                        ch1[x][y] +=1
                        last=0
                        break
                    elif last==0 and board[x][y]!=0:
                        last = board[x][y]
                        board[x][y]=0
                        ch1[x][y] +=1

            
            elif (abs(dx[i])>1 or abs(dy[i])>1):
                if 0<=x<=3 and 0<=y<=3 and board[x][y]!=0:
                    ch[x][y]+=1
                    ch1[x][y] = ch1[tmp[0]][tmp[1]]+1
                    Q.append((x,y))
                    if last!=0 and board[x][y]==last:
                        Q=[]
                        Q.append((x,y))
                        board[x][y]=0
                        ch1[x][y] +=1
                        last=0
                        break
                    if last==0 and board[x][y]!=0:
                        last = board[x][y]
                        board[x][y]=0
                        ch1[x][y] +=1
                elif 0<=x<=3 and 0<=y<=3:
                    if dx[i]>0:
                        x=3
                        y=tmp[1]
                    elif dx[i]<0:
                        x=0
                        y=tmp[1]
                    if dy[i]>0:
                        x=tmp[0]
                        y=3
                    elif dy[i]<0:
                        x=tmp[0]
                        y=0
                    ch[x][y]+=1
                    ch1[x][y] = ch1[tmp[0]][tmp[1]]+1
                    Q.append((x,y))

                    if last!=0 and board[x][y]==last:
                        Q=[]
                        Q.append((x,y))
                        board[x][y]=0
                        ch1[x][y] +=1
                        last=0
                        break
                    elif last==0 and board[x][y]!=0:
                        last = board[x][y]
                        board[x][y]=0
                        ch1[x][y] +=1

                

    
    return max(sum(ch1,[]))

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r=1
c=0
print(solution(board, r, c))
