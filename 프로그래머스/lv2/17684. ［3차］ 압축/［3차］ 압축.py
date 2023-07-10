def solution(msg):
    """
    T O B E O R N O T T O B E O R T O B E O R N O T
    """
    base = dict()
    answer = []
    for i in range(1, 27):
        base[chr(64+i)] = i
        
    # print(base)
    i=0
    while True:
        if len(msg) <= i:
            break
            
        j=2
        count = 0
        while True:
            if len(msg[i:i+j]) != j:
                answer.append(base[msg[i:i+j]])
                break
            elif not msg[i:i+j] in base:
                answer.append(base[msg[i:i+j-1]])
                base[msg[i:i+j]] = len(base) + 1
                break
            else:
                count += 1
            j+=1
            
        i+=1+count
        # print('here', "i", i, "j", j)

    # print(base)
    # print(answer)
    
    return answer