T = int(input())

for test_case in range(1, T + 1):
    t = int(input())
    nums = list(map(int, input().split()))
    num_count = {}

    for i in range(len(nums)):
        if nums[i] in num_count.keys():
            continue
        else:
            num_count[nums[i]] = nums.count(nums[i])

    max_count = max(num_count.values())
    result = max(score for score, cnt in num_count.items() if cnt == max_count)

    print(f"#{test_case} {result}")