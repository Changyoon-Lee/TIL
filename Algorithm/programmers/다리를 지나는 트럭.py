# 코딩테스트 연습 스택/큐 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    i=0
    bridge=[]
    sum_bridge=0
    while truck_weights:
        i+=1
        
        if weight-sum_bridge>=truck_weights[0]:# 다리에 올라갈수 있으면 올라감
            temp = truck_weights.pop(0)
            bridge.append((temp, i))
            sum_bridge+=temp
            
        else: # 무거워서 못올라가면 다리위 트럭중 젤 먼저출발한거 끝날때의 시간으로 넘어가서 다시 loop 시작
            temp = bridge.pop(0)
            sum_bridge-=temp[0]
            i = temp[1] + bridge_length-1
            continue


                
        if bridge[0][1] + bridge_length-1 == i: # 트럭이 하나 지나가면 무게 에서 제외시키기
            sum_bridge-=bridge.pop(0)[0]

    if bridge: #트럭이 다 올라 탔으면 제일 마지막에 올라탄거 끝날 떄의 시간을 return 함
        return bridge[-1][1] + bridge_length



print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))