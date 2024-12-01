def today2timestamp(date):
    year, month, day = map(int, date.split('.'))
    time = 0
    time += year * 28 * 12
    time += month * 28
    time += day
    return time
def solution(today, terms, privacies):
    now_timestamp = today2timestamp(today)
    dic = {}
    for term in terms:
        a,b = term.split()
        b = int(b)
        dic[a] = b
    
    answer = []
    for index, privacy in enumerate(privacies):
        date, a = privacy.split()
        privacy_timestamp = today2timestamp(date)
        privacy_timestamp += dic[a] * 28
        
        if privacy_timestamp <= now_timestamp:
            answer.append(index +1)
        
    return sorted(answer)