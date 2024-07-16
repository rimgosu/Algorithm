from collections import defaultdict

def solution(info, edges):
    answer = 0
    
    stack = []
    stack.append(0)
    
    node = {}
    for edge in edges:
        first = edge[0]
        second = edge[1]
        
        if not first in node:
            node[first] = []
        if not second in node:
            node[second] = []
        
        node[first].append(second)
        node[second].append(first)
        
    print(node)
    
    return answer