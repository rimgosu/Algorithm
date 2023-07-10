def toN(number, N):
    s= ""
    while True:
        if number < 1 :
            break
        
        if number % N == 10:
            s += 'A'
        elif number % N == 11:
            s += 'B'
        elif number % N == 12:
            s += 'C'
        elif number % N == 13:
            s += 'D'
        elif number % N == 14:
            s += 'E'
        elif number % N == 15:
            s += 'F'
        else:
            s += str(number % N)
        
        number = number // N
    
    return s[::-1]
    

def solution(n, t, m, p):
    """
    0 1 1 0 1 1 1 0 0 
    """
    st = "0"
    i=0
    while True:
        if len(st) >= 100000:
            break
        st += toN(i, n)
        i+=1
        
    # print(st)
    answer = ""
    i=0
    while True:
        if t <= len(answer):
            return answer
        if i % m == p-1:
            answer+=st[i]
        # print("i", i, "m", m, "p", p)
        i+=1
    

# print(solution(16, 99, 3, 2))