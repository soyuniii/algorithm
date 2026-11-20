def game(c1, c2):
    winning_rules = {(0,2),(1,0),(2,1)}
    if c1 == c2:
        print("Result : Draw")
    if (c1,c2) in winning_rules:
        print("Result : Man1 Win!")
    else:
        print("Result : Man2 Win!")


m1 = input()
m2 = input()

choice = {"가위":0,"바위":1,"보":2}

game(choice[m1],choice[m2])