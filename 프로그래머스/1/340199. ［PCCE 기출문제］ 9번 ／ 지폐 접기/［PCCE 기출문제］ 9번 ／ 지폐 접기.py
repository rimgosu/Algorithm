"""
1. 항상 긴쪽을 반으로 접음
2. 홀수면 소수점 이하는 버림
"""
def solution(wallet, bill):
    answer = 0
    
    while True:
        if max(bill) <= max(wallet) and min(bill) <= min(wallet):
            break
        
        half = max(bill) //2
        bill[bill.index(max(bill))] = half
        answer+=1
        
    return answer