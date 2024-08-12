def solution(skill, skill_trees):
    answer = 0
    for now_learn in skill_trees:
        stack = list(skill[::-1]).copy()
        possible = True
        
        for i in now_learn:
            
            if i in stack and i != stack[-1]:
                possible = False
                break

            if i == stack[-1]:
                stack.pop()
                
            if not stack:
                break
                
        if possible:
            answer +=1
    
    return answer
        