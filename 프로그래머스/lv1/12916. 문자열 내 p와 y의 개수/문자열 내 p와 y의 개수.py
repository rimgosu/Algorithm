def solution(s):
    p, y = 0, 0
    for _s in s:
        if _s.lower() == "p":
            p +=1
        elif _s.lower() == "y":
            y +=1
    
    answer = False
    if p == y :
        answer = True
    elif p == 0 and y == 0 :
        answer = False
    
    return answer