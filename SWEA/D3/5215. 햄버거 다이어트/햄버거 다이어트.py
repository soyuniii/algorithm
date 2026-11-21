def dfs(idx, t_sum, k_sum):
    if k_sum > l:
        return 0

    if idx == n:  # 모든 재료 다 살펴봤을때
        return t_sum

    t, k = choice[idx]
    include_taste = dfs(idx + 1, t_sum + t, k_sum + k)  # 선택한 경우
    exclude_taste = dfs(idx + 1, t_sum, k_sum)  # 선택 안한 경우

    return max(include_taste, exclude_taste)


T = int(input())

for test_case in range(1, T + 1):
    n, l = map(int, input().split()) # 재료수, 제한 칼로리
    choice = [tuple(map(int, input().split())) for _ in range(n)]

    best_taste = dfs(0,0,0)
    print(f"#{test_case} {best_taste}")
