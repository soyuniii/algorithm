from itertools import combinations
T = int(input())

for test_case in range(1, T + 1):
    n,k = map(int, input().split()) #부분집합 원소의 수 N, 부분 집합의 합 K
    a = [i for i in range(1,13)]
    result = 0
    
    for c in combinations(a, n):
        if sum(c) == k:
            result += 1
            
    print(f"#{test_case} {result}")
