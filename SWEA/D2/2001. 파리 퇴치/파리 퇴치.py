

T = int(input())

for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_flies = 0

    # 파리채 시작좌표 (r,c)순회
    for r in range(n-m+1):
        for c in range(n-m+1):
            current_sum = 0

            # (r,c)부터 m*m합 계산
            for dr in range(m):
                for dc in range(m):
                    current_sum += arr[r+dr][c+dc]

            if current_sum > max_flies:
                max_flies = current_sum

    print(f"#{test_case} {max_flies}")


