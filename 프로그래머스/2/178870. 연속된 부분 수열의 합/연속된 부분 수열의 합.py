from collections import defaultdict
# 슬라이딩 윈도우 사용
def solution(sequence, k):
    answer = []
    indexes = []
    a, b, endpoint, total = 0, 0, len(sequence) -1, sequence[0]
    
    # 만약 k값보다 합이 작으면 b+=1 
    # 만약 k값보다 합이 크면 a+=1
    # 만약 k값과 합이 같으면 해당 index들 저장, b+=1
    # 만약 b = endpoint: a 값 증가

    while a <= endpoint:
        if b == endpoint:
            if total == k:
                indexes.append((a,b))
            total -= sequence[a]
            a+=1
        elif total <= k:
            if total == k:
                indexes.append((a,b))
            b+=1
            total += sequence[b]
        elif total > k:
            total -= sequence[a]
            a+=1

    min_length = 9999999
    
    for i in indexes:
        a_temp, b_temp = i
        if min_length > b_temp-a_temp:
            min_length = b_temp-a_temp

    min_seq = []
    
    for i in indexes:
        a_temp, b_temp = i
        if min_length == b_temp-a_temp:
            min_seq.append(i)
    
    return [min(min_seq[0]), max(min_seq[0])]