def solution(n):
    result = ""
    while(n):
        result += str(n%10)
        n //= 10
    return int("".join(sorted(result, reverse=True)))