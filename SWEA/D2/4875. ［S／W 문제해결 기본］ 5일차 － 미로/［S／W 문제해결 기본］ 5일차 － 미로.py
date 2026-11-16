def dfs(start, maze, n):
    visited = [[False]*n for _ in range(n)]
    stack = [start]
    
    while stack:
        curr_r, curr_c = stack.pop()
        
        if maze[curr_r][curr_c] == 3:
            return 1
        
        visited[curr_r][curr_c] = True
        
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if (
                0 <= nr < n
                and 0 <= nc < n
                and maze[nr][nc] != 1
                and not visited[nr][nc]
            ):
                stack.append((nr, nc))
    return 0   

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    dr = [-1,1,0,0]  #상하
    dc = [0,0,-1,1] #좌우
    start = ()
    for r in range(n):
        for c in range(n):
            if maze[r][c] == 2:
                start = (r, c)
                break

    result = dfs(start, maze, n)
    print(f"#{test_case} {result}")
	                
