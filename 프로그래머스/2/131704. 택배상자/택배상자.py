def solution(order):
    answer = 0
    
    stack = [i+1 for i in range(len(order))]
    stack = stack[::-1]
    
    sub_stack = []
    
    for i in order:
        if stack and stack[-1] == i:
            stack.pop()
            answer +=1
        elif sub_stack and sub_stack[-1] == i:
            sub_stack.pop()
            answer +=1
        else:
            while stack:
                if stack[-1] == i:
                    break
                sub_stack.append(stack.pop())
            
            if stack and stack[-1] == i:
                stack.pop()
                answer+=1
            elif sub_stack and sub_stack[-1] == i:
                sub_stack.pop()
                answer+=1
            else:
                break
    
    return answer