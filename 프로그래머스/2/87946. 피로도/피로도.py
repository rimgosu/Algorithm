def solution (k, dungeons):
    answer = [0]
    def dfs(remain, visited):
        if answer[0] < sum(visited):
            answer[0] = sum(visited)
        for idx, dungeon in enumerate(dungeons):
            if dungeon[0] <= remain and not visited[idx]:
                visited[idx] = True
                dfs(remain - dungeon[1], visited)
                visited[idx] = False
                
    visited = [False] * len(dungeons)
    dfs(k, visited)
    return answer[0]