def solution(number, k):
    
    answer = ''
    stack = []
    for i in number:
        while stack and stack[-1] < i and k >0:
            stack.pop()
            k-=1
        stack.append(i)
        
    for i in range(k):
        stack.pop()
    
    return ''.join(stack)