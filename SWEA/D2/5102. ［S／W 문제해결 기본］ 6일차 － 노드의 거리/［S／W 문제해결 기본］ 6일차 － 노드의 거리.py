from collections import deque


T = int(input())

def bfs(start, graph, dist):
    q = deque([start])

    while q:
        cur = q.popleft()
        for nxt in graph[cur]: # 6 4
            if dist[nxt] == -1: # 미방문일때
                dist[nxt] = dist[cur] + 1
                q.append(nxt)


for test_case in range(1, T + 1):
    v,e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    s,g = map(int, input().split())

    dist = [-1]*(v+1) #출발점으로 부터의 거리 배열 만들기
    dist[s] = 0

    bfs(s, graph, dist)
    result = dist[g] if dist[g] != -1 else 0

    print(f"#{test_case} {result}")




