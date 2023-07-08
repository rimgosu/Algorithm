def to_ag(st):
    ag1 = []
    for i in range(len(st)-1):
        con = False
        tempstr = st[i:i+2]
        tempstr = tempstr.lower()
        # print(tempstr)
        for ts in tempstr:
            if ord(ts) >= 97 and ord(ts) <= 122:
                pass
            else:
                con = True
        
        if con:
            continue
        else:
            ag1.append(tempstr)
    return ag1

def solution(str1, str2):
    answer = 0
    ag1 = to_ag(str1)
    ag2 = to_ag(str2)
    # print(ag1, ag2)
    ag1set = set(ag1)
    ag2set = set(ag2)
    ag1set.update(ag2set)
    # print( ag1set)
    gyo = 0
    hap = 0 
    for s in ag1set:
        cnt1 = ag1.count(s)
        cnt2 = ag2.count(s)
        # print(min(cnt1, cnt2))
        gyo += min(cnt1, cnt2)
        hap += max(cnt1, cnt2)
    
    return ( gyo/hap ) * 65536 //1 if not (gyo == 0 and hap == 0) else 65536