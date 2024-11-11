n, length = map(int, input().split())

def dfs(now_string, count, remain):
    if count == length:
        print(now_string[1:])
    
    # 4개라고 가정
    # 1 2 3 5 left right
    #   2 3 5 [:0] [1:]
    # 1   3 5 [:1] [2:]
    # 1 2   5 [:2] [3:]

    for i in range(len(remain)):
        left = remain[:i]
        right = remain[i+1:]
        dfs(f'{now_string} {remain[i]}', count+1, left+right)

dfs('', 0, list(range(1,n+1)))