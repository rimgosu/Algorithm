def solution(n, wires):
    # 각각 하나씩 빼고,
    # 원소 [1,3] 하나씩 출발점으로 사용
    answer = 999
    for i in range(len(wires)):
        wires_copy = wires.copy()
        start_a, _ = wires_copy[i]
        del wires_copy[i]
        
        node_dic = {}
        for wire in wires_copy:
            a, b = wire
            if not a in node_dic.keys():
                node_dic[a] = []
            if not b in node_dic.keys():
                node_dic[b] = []
            node_dic[a].append(b)
            node_dic[b].append(a)
        
        visited = {}
        for i in range(n):
            visited[i+1] = False

        #bfs
        queue = []
        queue.append(start_a)
        visited[start_a] = True
        
        while queue:
            now = queue.pop(0)
            if now in node_dic.keys():
                for next_node in node_dic[now]:
                    if not visited[next_node]:
                        queue.append(next_node)
                        visited[next_node] = True
               
        visited_sum = sum(visited.values())
        another = n - visited_sum
        if abs(visited_sum - another) < answer:
            answer = abs(visited_sum - another)
    return answer