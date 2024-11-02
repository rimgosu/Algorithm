from collections import deque
import sys
input = sys.stdin.readline  # 빠른 입력 처리

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

# 간선 정보 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 인접 리스트 정렬
for i in range(1, N + 1):
    graph[i].sort()

# BFS
queue = deque([R])
visited[R] = 1
count = 1

while queue:
    v = queue.popleft()
    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            visited[i] = count
            queue.append(i)

# 빠른 출력 처리
print(*visited[1:], sep='\n')