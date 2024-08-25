def solution(k, m, score):
    answer = 0
    score.sort()
    temp_stack = []
    
    while score:
        temp_stack.append(score.pop())
        
        if len(temp_stack) == m:
            while temp_stack:
                answer += temp_stack[-1]
                temp_stack.pop(0)
    
    return answer