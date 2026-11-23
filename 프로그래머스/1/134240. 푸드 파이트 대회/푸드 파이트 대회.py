def solution(food):
    left = '' #122333
    for f, count in enumerate(food):
        # 음식(인덱스) * 개수(값)
        if f != 0:
            count //= 2
            left += str(f) * count

    return left + '0' + left[::-1]