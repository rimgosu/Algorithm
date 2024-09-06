def solution(storey):
    answer = 0
    
    while storey:
        digit = storey % 10
        next_digit = (storey // 10) % 10
        
        if digit > 5 or (digit == 5 and next_digit >= 5):
            answer += (10 - digit)
            storey += 10
        else:
            answer += digit
        
        storey //= 10
    
    return answer