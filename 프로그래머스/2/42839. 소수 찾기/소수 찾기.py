"""
numbers 만큼 자리가 있다고 생각하자.
ex) 1234
_ _ _ _
1. x 1 2 3 4 (1선택)
2. 2 3 4 (2선택)
3. 3 4 (3선택)
4. 4 (4선택)

- 애초에 x를 한번이라도 고르지 않았다면 x 선택지는 제외됨

1. x 1 2 3 4 (x선택)
2. x 1 2 3 4 (x선택)
3. x 1 2 3 4 (x선택)
4. x 1 2 3 4 (1선택)

이런식으로 숫자 만드는 것임.
"""
import math

def is_prime(number):
    for i in range(2,math.floor(number ** 0.5)+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    length = len(numbers)
    
    repository = []
    
    def dfs(now_number, remain):

        if len(now_number) == length:
            return repository.append(now_number)
        
        for i in remain:
            if i == 'x':
                dfs(now_number+i, remain)
            else:
                next_remain = remain.copy()
                if 'x' in remain:
                    next_remain.remove('x')
                next_remain.remove(i)
                dfs(now_number+i, next_remain)
            
    remain = ['x']
    for i in numbers:
        remain.append(i)

    dfs('', remain)
    
    trimed_repository = set()
    for number_comb in repository:
        number = ''
        for i in number_comb:
            if i != 'x':
                number += i
        if number:
            trimed_repository.add(int(number))
    
    trimed_repository.discard(0)
    trimed_repository.discard(1)

    for i in trimed_repository:
        if is_prime(i):
            answer += 1
    
    return answer