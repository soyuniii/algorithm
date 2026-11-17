def divide(start, end,cards):
    if start == end:
        return start
    
    mid = (start + end) // 2
    
    left_winner = divide(start, mid, cards)
    right_winner = divide(mid+1, end, cards)
    
    return pick(left_winner, right_winner, cards)

        
# 가위바위보 함수 
def pick(p1, p2, cards):
    c1 = cards[p1]
    c2 = cards[p2]
    
    if c1 == c2:
        return p1 if p1<p2 else p2
    
    # 가위 바위
    elif c1 == 1 and c2 == 2:
        return p2
    elif c1 == 2 and c2 == 1:
        return p1
    
    # 바위 보
    elif c1 == 2 and c2 == 3:
        return p2
    elif c1 == 3 and c2 == 2:
        return p1
    
    #보 가위
    elif c1 == 3 and c2 == 1:
        return p2
    elif c1 == 1 and c2 == 3:
        return p1
    
    
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    cards = list(map(int, input().split()))

    winner = divide(0, len(cards)-1, cards)
    
    print(f"#{test_case} {winner + 1}") # 학생 번호는 1번부터

