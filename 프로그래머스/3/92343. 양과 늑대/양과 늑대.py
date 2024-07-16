def solution(info, edges):
    from collections import defaultdict

    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)

    def dfs(node, sheep, wolf, next_nodes):
        if info[node] == 0:
            sheep += 1
        else:
            wolf += 1

        if wolf >= sheep:
            return 0

        max_sheep = sheep

        for i in range(len(next_nodes)):
            next_node = next_nodes[i]
            new_next_nodes = next_nodes[:i] + next_nodes[i+1:] + graph[next_node]
            max_sheep = max(max_sheep, dfs(next_node, sheep, wolf, new_next_nodes))

        return max_sheep

    return dfs(0, 0, 0, graph[0])

# 예제 테스트 케이스
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))  # 출력 예시: 5
