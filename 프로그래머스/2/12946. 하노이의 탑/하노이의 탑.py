lst = []

def hanoi(n,fr,mid,to):
    if n == 1:
        lst.append([fr,to])
    else:
        hanoi(n-1,fr,to,mid)
        lst.append([fr,to])
        hanoi(n-1,mid,fr,to)

def solution(n):
    hanoi(n,1,2,3)
    return lst