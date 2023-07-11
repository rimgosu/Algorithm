def solution(record):
    answer = []
    rDict = {}
    for r in record:
        rList = r.split(" ")
        if rList[0] == 'Enter':
            rDict[rList[1]] = rList[2]
        elif rList[0] == 'Change':
            rDict[rList[1]] = rList[2]
        else:
            pass
        # print(rList)
        
    for r in record:
        rList = r.split(" ")
        if rList[0] == 'Enter':
            # print(rDict[rList[1]])
            answer.append(rDict[rList[1]]+"님이 들어왔습니다.")
        elif rList[0] == 'Leave':
            answer.append(rDict[rList[1]]+"님이 나갔습니다.")
    # print(rDict)
    return answer