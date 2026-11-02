def solution(numbers):
    result = 0
    for i in range(0,10):
        if i in numbers:
            continue
        else:
            result += i
    return result