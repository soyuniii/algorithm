T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    cards = list(map(int, input()))
    cards_count = {} #key: card, value:count
    
    for card in cards:
        cards_count[card] = cards.count(card)
    
    # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽 고르기 
    result = max(cards_count.items(), key=lambda x: (x[1], x[0]))
       
    print(f"#{test_case} {result[0]} {result[1]}")
