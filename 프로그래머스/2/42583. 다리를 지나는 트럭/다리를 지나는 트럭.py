def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    in_progress = []
    status = []
    while True:
        # print(in_progress, status, truck_weights)
        if not in_progress and not truck_weights:
            break
        
        if truck_weights:
            truck = truck_weights[0]
            if truck + sum(in_progress) <= weight:
                truck_weights.pop(0)
                in_progress.append(truck)
                status.append(0)
        
        # status + 1, 만약 bridge_length와 같다면 삭제
        del_index = []
        for i in range(len(status)):
            status[i] = status[i] + 1
            if status[i] == bridge_length:
                del_index.append(i)
        
        for i in del_index:
            del status[i]
            del in_progress[i]
                
        answer +=1
    
    return answer +1 