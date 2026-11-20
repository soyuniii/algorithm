p1 = input()
p2 = input()
c1 = input()
c2 = input()

winning_rules = {("가위","보"),("바위","가위"),("보","바위")}

if (c1, c2) in winning_rules:
    print(f"{c1}가 이겼습니다!")
else:
    print(f"{c2}가 이겼습니다!")
