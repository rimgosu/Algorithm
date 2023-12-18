def solution(survey, choices):
    answer = ''
    
    # 성격 유형 검사
    # 1. R,T
    # 2. C,F
    # 3. J,M
    # 4. A,N
    
    # 1	매우 비동의
    # 2	비동의
    # 3	약간 비동의
    # 4	모르겠음
    # 5	약간 동의
    # 6	동의
    # 7	매우 동의
    
    # 1번째 캐릭터 : 비동의
    # 2번째 캐릭터 : 동의
    
    R,T = 0,0
    C,F = 0,0
    J,M = 0,0
    A,N = 0,0
    
    dic = dict(
        R=0,T=0,C=0,F=0,J=0,M=0,A=0,N=0
    )
    
    for s,c in zip(survey, choices):
        if c == 1:
            dic[s[0]] +=3
        if c == 2:
            dic[s[0]] +=2
        if c == 3:
            dic[s[0]] +=1
        if c == 5:
            dic[s[1]] +=1
        if c == 6:
            dic[s[1]] +=2
        if c == 7:
            dic[s[1]] +=3
                
    print(dic)
    
    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
        
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    print(answer)
    
    return answer