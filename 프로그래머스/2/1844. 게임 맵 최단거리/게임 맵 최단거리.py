from collections import deque

def bfs(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

    answer = 1
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if x == n-1 and y == m-1:
                return answer
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        answer += 1

    return -1

def solution(maps):
    return bfs(maps)
