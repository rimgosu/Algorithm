def solution(board):
    answer = 0
    width, height = len(board[0]), len(board)
    print(width, height)
    directions = [(0,1),(1,1),(1,0),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]
    for y in range(height):
        for x in range(width):
            if board[y][x] == 1:
                for dx, dy in directions:
                    if 0 <= dx + x < width and 0 <= dy+ y < height and board[y+dy][x+dx] == 0:
                        board[y+dy][x+dx] = -1
    
    for y in range(height):
        for x in range(width):
            if board[y][x] == 0:
                answer +=1
    return answer