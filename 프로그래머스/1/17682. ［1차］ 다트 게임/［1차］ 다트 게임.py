def solution(dartResult):
    answer = 0
    length = len(dartResult)
    lst, prev = [], ''
    for i in range(length):
        if dartResult[i] in 'SDT':
            if dartResult[i] == 'D':
                lst.append(int(prev) ** 2)
            elif dartResult[i] == 'T':
                lst.append(int(prev) ** 3)
            else:
                lst.append(int(prev))
            prev = ''
        elif dartResult[i] == '*':
            lst[-1] *= 2
            try:
                lst[-2] *= 2
            except:
                pass
        elif dartResult[i] == '#':
            lst[-1] = -lst[-1]
        else:
            prev += dartResult[i]
    return sum(lst)