def solution(babbling):
    answer = 0
    
    # 발음할 수 있는 것 : aya, ye, woo, ma
    # 같은 발음 연속으로 못함 : yeye
    
    can_babbling = ['aya', 'ye', 'woo', 'ma']
    
    
    for b in babbling:
        isBabbling = False
        b_copy = b
        key = ''
        while True:
            print(b_copy)
            if b_copy[:2] == key:
                isBabbling = False
                break
            elif b_copy[:3] == key:
                isBabbling = False
                break
            elif b_copy[:3] == 'aya':
                b_copy = b_copy[3:]
                key = 'aya'
            elif b_copy[:3] == 'woo':
                b_copy = b_copy[3:]
                key = 'woo'
            elif b_copy[:2] == 'ye':
                b_copy = b_copy[2:]
                key = 'ye'
            elif b_copy[:2] == 'ma':
                b_copy = b_copy[2:]
                key = 'ma'
            elif b_copy == '':
                isBabbling = True
                break
            else:
                isBabbleing = False
                break
        
        if isBabbling:
            answer +=1
    
    
            
            
        
    return answer