T = int(input())

for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    v = list(map(int, input().split()))
    
    sums = []
    for i in range(n-m+1):
        current_sum = sum(v[i:i+m])
        sums.append(current_sum)
    
    result = max(sums) - min(sums)
    
    print(f"#{test_case} {result}")