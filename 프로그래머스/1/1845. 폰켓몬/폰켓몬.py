def solution(nums):
    count = len(nums)//2
    if len(set(nums)) >= count:
        return count
    else:
        return len(set(nums))