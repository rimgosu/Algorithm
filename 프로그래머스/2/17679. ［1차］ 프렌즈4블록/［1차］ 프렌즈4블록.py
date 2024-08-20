# 1. stack에 m-1, n-1 만큼 원소를 넣음
# 2. 우, 하, 우하 본인과 같은지 검사
# 3. stack 모두 털면 블럭 삭제 - *으로 변경
# 4. 남아 있는 블럭 아래로 치환
# 5. 1-4 반복, 모두 검사했는데 사라질 블럭 없다면 종료

def solution(m, n, board):
    answer = 0
    
    new_board = [[] for i in range(m)]
    for i in range(m):
        for j in range(n):
            new_board[i].append(board[i][j])
            
    while True:
        stack = []
        delete_queue = []
        for i in range(n-1):
            for j in range(m-1):
                stack.append((i,j))

        stack = stack[::-1]

        while stack:
            directions = [(1,0), (0,1), (1,1)]
            x,y = stack.pop()

            element = new_board[y][x]

            can_delete = True

            for dx,dy in directions:
                if new_board[y+dy][x+dx] == '*' or element != new_board[y+dy][x+dx]:
                    can_delete = False
                    break

            if can_delete:
                delete_queue.append((x,y))
        
        if not delete_queue:
            break

        while delete_queue:
            directions = [(0,0), (1,0), (0,1), (1,1)]
            x, y = delete_queue.pop()
            for dx, dy in directions:
                if new_board[y+dy][x+dx] != '*':
                    new_board[y+dy][x+dx] = '*'
                    answer +=1

        for i in range(n):
            tmp = []
            for j in range(m):
                tmp.append(new_board[j][i])

            idx = -1
            for j in range(m-1,-1,-1):
                if tmp[j] != '*':
                    tmp[j], tmp[idx] = tmp[idx], tmp[j]
                    idx -= 1

            for j in range(m):
                new_board[j][i] = tmp[j]
        
    return answer