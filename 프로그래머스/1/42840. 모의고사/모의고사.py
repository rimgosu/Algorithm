def solution(answers):
    lsts = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    corrects = [0, 0, 0]
    for index, answer in enumerate(answers):
        for lst_index, lst in enumerate(lsts):
            if lst[index % len(lst)] == answer:
                corrects[lst_index] +=1
    
    ans_lst = [index +1 for index, correct in enumerate(corrects) if correct == max(corrects)]
    ans_lst.sort()
    return ans_lst