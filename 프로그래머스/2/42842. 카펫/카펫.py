from itertools import permutations
def solution(brown, yellow):
    # 아이디어: 갈+노 = 넓이
    size = brown + yellow
    # 노란색 개수로 만들 수 있는 조합찾기 (가로,세로) -> 약수성질?
    for h in range(1, int(yellow**0.5)+1):
        if yellow % h == 0:
            w = yellow // h
            if (w+2) * (h+2) == size:
                return [w+2, h+2]
                