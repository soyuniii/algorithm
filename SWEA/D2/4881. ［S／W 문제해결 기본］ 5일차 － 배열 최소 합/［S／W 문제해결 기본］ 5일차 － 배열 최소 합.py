def dfs(row, current_sum, visited):
    global min_sum
    
    if current_sum >= min_sum: # 가지치기
        return
    
    if row == n:
        if current_sum < min_sum:
             min_sum = current_sum
        return
    
    for col in range(n):  
        if not visited[col]:
            visited[col] = True
            dfs(row+1, current_sum+ls[row][col], visited)
            visited[col] = False

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    ls = [list(map(int, input().split())) for _ in range(n)]
    visited = [False]*n # 방문한 열인지 확인용
    min_sum = float('inf')
    dfs(0, 0,visited)
    
    print(f"#{test_case} {min_sum}")