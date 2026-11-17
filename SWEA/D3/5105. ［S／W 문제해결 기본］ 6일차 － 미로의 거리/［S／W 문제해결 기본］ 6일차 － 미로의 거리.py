from collections import deque

def bfs(start, maze):
    q = deque([(start[0], start[1], 0)]) #r, c, 이동거리
    visited = [[False]*n  for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    while q:
        curr_r, curr_c, dist = q.popleft()
        
        if maze[curr_r][curr_c] == 3:
            return dist - 1 # 미로 이동 칸 수 (시작점 제외)
        
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if (
                0<= nr < n
                and 0<= nc < n
                and maze[nr][nc] != 1
                and not visited[nr][nc]
               ):
                visited[nr][nc] = True # 큐 넣기 전 방문처리
                q.append((nr,nc, dist+1))

    return 0
    
T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    start = ()
    dr = [-1,1,0,0] #상하
    dc = [0,0,-1,1] #좌우
    
    # 시작점 찾기
    for r in range(n):
        for c in range(n):
            if maze[r][c] == 2:
                start = (r,c)
                
    # 최소 거리 -> bfs
    # 미로 이동 최소 칸 수, 경로 없으면 0
    result = bfs(start, maze) 
    
    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
