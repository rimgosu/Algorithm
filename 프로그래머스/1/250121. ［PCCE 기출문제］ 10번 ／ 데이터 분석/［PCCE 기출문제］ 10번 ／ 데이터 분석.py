def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    ext_lst = ['code', 'date', 'maximum', 'remain']
    
    for i in data:
        if ext == ext_lst[0] and i[0] < val_ext:
            answer.append(i)
        elif ext == ext_lst[1] and i[1] < val_ext:
            answer.append(i)
        elif ext == ext_lst[2] and i[2] < val_ext:
            answer.append(i)
        elif ext == ext_lst[3] and i[3] < val_ext:
            answer.append(i)
            
    answer.pop(0)
    
    if sort_by == ext_lst[0]:
        answer.sort(key=lambda x:x[0])
    elif sort_by == ext_lst[1]:
        answer.sort(key=lambda x:x[1])
    elif sort_by == ext_lst[2]:
        
        answer.sort(key=lambda x:x[2])
    else:
        answer.sort(key=lambda x:x[3])
            
    
    return answer