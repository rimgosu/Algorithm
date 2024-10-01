def solution(n):
    answer = 0
    
    lst, i = [], 1
    while len(lst) <= 100:
    # for _ in range(100):
        # 3의 배수인 경우
        if i % 3 == 0:
            i += 1
            continue
        
        # 문자열 3이 포함된 경우
        is_continue = False
        for str_i in str(i):
            if str_i == '3':
                is_continue = True
                break
        
        if is_continue:
            i += 1
            continue
        
        lst.append(i)
        i += 1
    
    # print(lst)
    
    return lst[n-1]