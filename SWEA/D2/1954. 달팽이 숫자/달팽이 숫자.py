#import sys
#sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    dr = [0,1,0,-1] #우하좌상 순
    dc = [1,0,-1,0]

    r,c = 0,0 #현재 위치
    direction = 0 #우:0 하:1 좌:2 상:3

    for num in range(1, n*n+1):
        arr[r][c] = num

        # 다음 이동 위치
        nr = r + dr[direction]
        nc = c + dc[direction]

        #방향 전환 조건
        #1. 배열 범위 벗어나거나
        #2. current != 0
        if nr < 0 or nr >= n or nc < 0 or nc >= n or arr[nr][nc] != 0:
            direction = (direction + 1) % 4
            # 방향 꺾은 위치로 갱신
            nr = r + dr[direction]
            nc = c + dc[direction]
        # 다음 위치로 이동
        r,c = nr,nc

    print(f"#{test_case}")
    for row in arr:
        print(*row)