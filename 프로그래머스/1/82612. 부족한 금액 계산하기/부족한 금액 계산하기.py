def solution(price, money, count):
    answer = money - sum(price*(i+1) for i in range(count)) #부족금액 (-)
    return 0 if answer > 0 else -answer