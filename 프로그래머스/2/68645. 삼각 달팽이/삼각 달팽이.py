def solution(n):
    table = [[0]*(i+1) for i in range(n)]
    dr = [1,0,-1]
    dc = [0,1,-1]
    
    r,c = 0,0
    dir = 0
    num = 1
    total_cnt = n*(n+1)//2
    
    while num <= total_cnt:
        table[r][c] = num
        num += 1
        
        # 다음으로 갈 칸
        nr = r + dr[dir]
        nc = c + dc[dir]
        
        if nr < 0 or nr >= n or nc < 0 or nc > nr or table[nr][nc] != 0:
            dir = (dir+1)%3
            nr = r + dr[dir]
            nc = c + dc[dir]
            
        r,c = nr, nc
    
    result = []
    for row in table:
        for val in row:
            result.append(val)
            
    return result
    
    