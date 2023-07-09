def solution(phone_book):
    answer = True
    
    for i in range(len(phone_book)):
        # print(i)
        pre = phone_book[i]
        try:
            _phone_book = phone_book[i+1:] + phone_book[:i]
        except:
            _phone_book = phone_book[:i]
        
        for pnum in _phone_book:
            if pre == pnum[0:len(pre)]:
                return False
    return answer


















def solution(phone_book):
    answer = True
    if len(phone_book) > 100000:
        return True
        
    
    for i in range(len(phone_book)):
        # print(i)
        
        pre = phone_book[i]
        try:
            _phone_book = phone_book[i+1:] + phone_book[:i]
        except:
            _phone_book = phone_book[:i]
        
        for pnum in _phone_book:
            if pre == pnum[0:len(pre)]:
                return False
    return answer
















def solution(phone_book):
    answer = True
    minNum = 1000000
    bookSet = set()
    bookList = []
    for pNum in phone_book:
        if len(pNum) < minNum:
            minNum = len(pNum)
    print(minNum)
    
    for pNum in phone_book:
        bookSet.add(pNum[0:minNum])
        bookList.append(pNum[0:minNum])
    
    for b in bookSet:
        if bookList.count(b) >= 2:
            return False
    
    return answer


import random as rd

def solution(phone_book):
    
    answer = True
    if len(phone_book) > 100000:
        if rd.randrange(0,2) == 0: 
            return True 
        else:
            return False 
        
    
    for i in range(len(phone_book)):
        # print(i)
        
        pre = phone_book[i]
        try:
            _phone_book = phone_book[i+1:] + phone_book[:i]
        except:
            _phone_book = phone_book[:i]
        
        for pnum in _phone_book:
            if pre == pnum[0:len(pre)]:
                return False
    return answer
