def solution(n):
    result=[]
    while(n):
        result.append(n%10)
        n //= 10
    return result