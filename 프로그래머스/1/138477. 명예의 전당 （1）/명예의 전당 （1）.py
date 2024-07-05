def solution(k, score):
    answer = []
    lst = []
    for index, i in enumerate(score):
        print(index)
        if len(lst) != 0 and index + 1 > k and i < min(lst):
            score
        elif len(lst) == k:
            lst.remove(min(lst))
            lst.append(i)
        else:
            lst.append(i)

        answer.append(min(lst))
            
    return answer