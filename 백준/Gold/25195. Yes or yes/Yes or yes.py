import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split()) # 정점, 간선

one_way_dict = {}
for i in range(m):
    a,b = map(int,input().split())
    
    if not a in one_way_dict.keys():
        one_way_dict[a] = []
    
    one_way_dict[a].append(b)

fan_count = int(input())
fans = list(map(int, input().split()))

# visited: 개별로 존재해야 함
visited_dict = {}
for i in range(n):
    visited_dict[i+1] = False

visited_dict[1] = True
start=1

answer = ["Yes"]

def dfs(where, visited, encountered):
    if encountered or where in fans:
        return 
    else:
        # 더이상 방문 못하면
        # 간선 봤을 때 간선이 모두 방문했으면
        # answer를 "yes"로 변경한다.
        dict = one_way_dict.get(where, [])
        can_go = False
        for next in dict:
            if not visited[next]:
                can_go = True
                continue   
        
        if not can_go:
            answer[0] = "yes"
        
        if can_go:
            dict = one_way_dict.get(where, [])
            for next in dict:
                visited[next] = True
                if next in fans:
                    encountered = True
                dfs(next, visited, encountered)
                visited[next], encountered = False, False

dfs(1,visited_dict, False)
print(answer[0])