T = int(input())

for test_case in range(1,T+1):
    n, k = map(int, input().split())  #크기, 단어길이
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    # 0 불가 1가능
    answer = 0

    # 가로 검사
    for r in range(n):
        cnt = 0
        for c in range(n):
            if puzzle[r][c] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0
        if cnt == k:  # 행 끝까지 이어진 경우
            answer += 1
    # 세로방향 검사
    for c in range(n):
        cnt = 0
        for r in range(n):
            if puzzle[r][c] == 1:
                cnt += 1
            else:
                if cnt == k:
                    answer += 1
                cnt = 0
        if cnt == k:
            answer += 1

    print(f"#{test_case} {answer}")


