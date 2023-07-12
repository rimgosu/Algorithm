def solution(fees, records):
    answer = []
    dic = {}
    dicfee = {}
    for record in records:
        r = record.split()
        if r[1] in dic:
            a=list(map(int, dic[r[1]].split(":")))
            b=list(map(int, r[0].split(":")))
            totalTimeA = a[0] * 60 + a[1]
            totalTimeB = b[0] * 60 + b[1]
            if r[1] in dicfee:
                dicfee[r[1]] += abs(totalTimeA-totalTimeB)
            else:
                dicfee[r[1]] = abs(totalTimeA-totalTimeB)
            dic.pop(r[1])
        else:
            dic[r[1]] = r[0]
    

    for carnum, value in dic.items():
        a = list(map(int, value.split(":")))
        _a = a[0] * 60 + a[1]
        b = 23 * 60 + 59
        if carnum in dicfee:
            dicfee[carnum] += abs(_a-b)
        else:
            dicfee[carnum] = abs(_a-b)
            
    sortedkeys = sorted(dicfee.keys())
    newFeedict = {}
    # print(sortedkeys)
    for sk in sortedkeys:
        newFeedict[sk] = dicfee[sk]
    
    # print(newFeedict)
        
    for index, value in newFeedict.items():
        if value <= fees[0]:
            answer.append(fees[1])
        else:
            value -= fees[0]
            if value % fees[2] == 0:
                answer.append(fees[1] + (value // fees[2]) * fees[3])
            else:
                answer.append(fees[1] + (value // fees[2]) * fees[3] + fees[3])
    
    # print(dicfee)
    return answer