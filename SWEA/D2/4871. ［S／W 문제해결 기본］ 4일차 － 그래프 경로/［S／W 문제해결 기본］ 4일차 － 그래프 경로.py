def dfs (node, target, graph, visited):
    if node == target:
        return 1   
    visited[node] = True
    
    for next_node in graph[node]:
        if not visited[next_node]:
            if dfs(next_node, target, graph, visited):
                return 1
    return 0
            
T = int(input())

for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    graph =[[] for _ in range(v+1)]
    for _ in range(e):
        start, end = map(int, input().split())
        graph[start].append(end)
        
    s, g = map(int, input().split())
    
    visited = [False] * (v+1)
    
    result = dfs(s, g, graph, visited)
    print(f"#{test_case} {result}")
    
    