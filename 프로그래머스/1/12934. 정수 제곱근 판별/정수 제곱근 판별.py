def solution(n):
    x = n ** 0.5
    return -1 if not x.is_integer() else int((x+1)**2)
    