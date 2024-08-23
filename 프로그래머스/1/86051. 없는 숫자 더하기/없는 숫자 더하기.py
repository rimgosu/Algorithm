def solution(numbers):
    answer = 0
    
    numbers = set(numbers)
    numbers_all = set()
    for i in range(10):
        numbers_all.add(i)
    
    for number in numbers:
        numbers_all.discard(number)
    
    for i in numbers_all:
        answer += i
    
    return answer