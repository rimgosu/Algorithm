def solution(n):
    answer = ""
    s = str(n)
    lst = []
    for _s in s:
        lst.append(int(_s))
    
    lst.sort()
    print(lst)
    while True:
        if lst == []:
            break
            
        answer += str(lst.pop())
        
        
    return int(answer)