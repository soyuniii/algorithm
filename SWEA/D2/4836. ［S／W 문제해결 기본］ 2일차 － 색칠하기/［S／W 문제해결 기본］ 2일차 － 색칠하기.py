T = int(input())

for test_case in range(1, T + 1):
    n = int(input()) # 칠할 영역의 수
    board = [[0]*10 for _ in range(10)]
    purple = 0
    # 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color
    # color = 1 (빨강), color = 2 (파랑)
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if board[r][c] != 0:
                    purple += 1
                board[r][c] = color

    print(f"#{test_case} {purple}")
        
    
