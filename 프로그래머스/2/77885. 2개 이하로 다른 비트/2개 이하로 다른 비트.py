# 1. number의 2진수를 구한다.
# [
    # 2. +1씩 더해가며 {수:2진수} 꼴로 만든다.
    # 3. 차이를 비교한다.
# ]

def tenToTwo(number: int) -> str:
    two = ''
    while True:
        if number <= 1:
            two += str(number)
            break
        remain = number % 2
        number = number // 2
        
        two += str(remain)
        
    return two[::-1]

def twoToTen(string: str) -> int:
    number = 0
    for i in range(len(string)):
        number += 2 ** (len(string) -1 - i ) if string[i] == '1' else 0
        
    return number
        

def solution(numbers):
    answer = []
    
    for number_10 in numbers:
        plus = True
        
        number_2 = tenToTwo(number_10)
        
        if number_2[-1] == '0':
            answer.append(number_10 +1)
        else:
            idx = -1 # -3
            length = len(number_2) # -3
            list_2 = list(number_2)
            
            one_length = 0
            while True:
                if idx <= -length:
                    one_length = length
                    break
                if list_2[idx] == '0':
                    one_length = -idx -1
                    break
                idx -= 1
            
            # one_length -1 지점 1로 변경, one_length 지점 0으로
            # 만약 one_length == -length -> 앞에 1추가, one_length 지점 0으로
            
            if one_length == length:
                list_2 = list_2[::-1]
                list_2.append('1')
                list_2 = list_2[::-1]
                list_2[-one_length] = '0'
            else:
                list_2[-one_length-1] = '1'
                list_2[-one_length] = '0'
                
            new_number_2 = ''
            for i in list_2:
                new_number_2 += i
            answer.append(twoToTen(new_number_2))
            
    
    return answer