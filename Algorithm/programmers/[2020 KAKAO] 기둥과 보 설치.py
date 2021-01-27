from collections import defaultdict

def solution(n, build_frame):
    #[x,y, 구조물종류(0:기둥, 1:보), 설치여부(0:삭제, 1:설치)]
    
    #기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
    # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
    # 만족안돼는 지시사항은 무시
    def check_bo(x,y, first=0):
        if y==0 : return False # 이거 딱히 안필요한듯
        if board_dict[(x,y)]==2 or first==1:
            if board_dict[(x, y-1)] == 1 or board_dict[(x+1, y-1)] == 1:
                return True
            elif board_dict[(x-1, y)] ==2 and board_dict[(x+1, y)] == 2:
                return True
            return False
        else : return True
                
    def check_kidung(x,y, first=0):
        if board_dict[(x,y)]==1 or first==1:
            if y==0 or board_dict[(x, y-1)]==1 or board_dict[(x-1,y)]==2:
                return True
            return False
        else : return True

    board_dict=defaultdict(int)
    for i in build_frame:
        if i[3]==1:
            if i[2]==0: 
                # y값이 0이거나 밑에 기둥이 있는지?
                if check_kidung(i[0],i[1],1):
                    board_dict[(i[0], i[1])] = i[2]+1
            else:
                if check_bo(i[0],i[1], 1):
                    board_dict[(i[0], i[1])] = i[2]+1
        
        else :
            if i[2]==0:# 기둥없엘때
                board_dict[(i[0], i[1])] = 0
                if (check_kidung(i[0], i[1]+1) and check_bo(i[0]-1,i[1]+1) and check_bo(i[0],i[1]+1)) != True:
                    board_dict[(i[0], i[1])] = 1
            else: # 보 없엘때
                board_dict[(i[0], i[1])] = 0
                if (check_kidung(i[0]+1, i[1]) and check_bo(i[0]-1,i[1]) and check_bo(i[0]+1,i[1])) !=True:
                    board_dict[(i[0], i[1])] = 2
    res=[]
    for key, value in board_dict.items():
        if value != 0:
            res.append([key[0],key[1],value-1])
    res = sorted(res, key = lambda x: (x[0],x[1],x[2]))
    return res

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
	# [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]