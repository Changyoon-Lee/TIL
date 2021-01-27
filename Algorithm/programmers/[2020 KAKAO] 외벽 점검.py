from collections import deque
from itertools import permutations
def solution(n, weak, dist):
    
    dist.sort(reverse=True)
    
    for i in range(0, len(dist)):
        for j in permutations(dist[1:i+1]):
            worker = dist[:1]+list(j) # worker 수 몇명인지 여기서 결정
            print(worker)
            for _ in range(len(weak)): # 어느지점부터 시작할지 경우의 수 만큼 반복
                w=0
                weak_ = deque(weak)
                start = weak_.popleft() # 여기부터 worker가 일 시작
                while weak_: # weak_를 다 처리 할때까지 반복
                    chk = weak_.popleft()
                    if chk <= start+worker[w]:
                        continue
                    else :
                        start = chk
                        w+=1 # 다음 일꾼으로 넘어감
                        if w == len(worker): # 일꾼 부족하면 break
                            weak = weak[1:]+[n+weak[0]] # weak의 순서를 한칸 옮겨서 리스트를 만듬, n 더하여 뒤에 붙인다
                            break
                else : return(len(worker))
                
            

    else : return -1
    

print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))