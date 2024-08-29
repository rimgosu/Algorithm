from collections import defaultdict

def solution(weights):
    answer = 0
    
    weights.sort()
    
    weight_count = {}
    
    for weight in weights:
        if weight in weight_count:
            weight_count[weight] +=1
        else:
            weight_count[weight] = 1
    
    for key, value in weight_count.items():
        if value > 1:
            answer += value * (value -1) / 2
        
        for ratio in [2, 3/2, 4/3]:
            if key * ratio in weight_count:
                answer+= value * weight_count[key * ratio]
    
    return answer