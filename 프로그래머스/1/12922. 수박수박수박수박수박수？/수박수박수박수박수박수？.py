def solution(n):
    result = ''
    while(n):
        if result == '' or result[-1] == '박':
            result += '수'
        else:
            result += '박'
        n -= 1
    return result