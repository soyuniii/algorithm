T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    result = []
	
    for _ in range(len(nums)//2):
        mx = max(nums)
        mn = min(nums)
        result.append(mx)
        nums.remove(mx)
        result.append(mn)
        nums.remove(mn)
        
    print(f"#{test_case}", *result[:10])