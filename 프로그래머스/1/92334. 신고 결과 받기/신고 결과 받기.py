def solution(id_list, report, k):
    answer = []
    
    for i in range(len(id_list)):
        answer.append(0)
        
    
    report = list(set(report))
    
    dic_num = {}
    dic = {}
    
    for i in id_list:
        dic_num[i] = 0
        dic[i] = []

    
    for i in report:
        user, reported = i.split(' ')
        dic[user].append(reported)
        dic_num[reported] += 1

    
    stop_lst = []
    for key,value in dic_num.items():
        
        if value >= k:
            stop_lst.append(key)

    i=0
    for key,value in dic.items():
        for j in stop_lst:
            if j in value:
                answer[i] += 1
                
        i+=1
                
                
        
    return answer