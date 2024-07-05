def solution(s):
    answer = []
    dic = {}
    
    for i in s:
        
        if i in dic:
            answer.append(dic[i])
            dic[i] = 0
        else:
            dic[i] = 0
            answer.append(-1)
        
        for j in dic:
            dic[j] += 1
    
    return answer