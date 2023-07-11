def solution(scoville, K):
    answer = 0
    scoville.sort(reverse = True)
    # print(scoville)
    
    while True:
        if scoville[-1] < K and len(scoville) == 1:
            return -1
        if scoville[-1] >= K:
            break
        
        a = scoville.pop()
        b = scoville.pop()
        
        temp = [a+b*2]
        
        while True:
            
            if scoville == []:
                scoville= temp
                break
            
            if scoville[-1] >= a+b*2:
                scoville.extend(temp)
                break
            
            if scoville[-1] < a+b*2:
                temp.append(scoville.pop())
        
        answer +=1
        scoville.sort(reverse = True)
    
    return answer





import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) 
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + (min2 * 2)
        heapq.heappush(scoville, new_scoville)
        
        answer += 1
    
    return answer