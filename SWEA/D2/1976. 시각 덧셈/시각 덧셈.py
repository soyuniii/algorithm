T = int(input())

for test_case in range(1,T+1):
    h1,m1,h2,m2 = map(int, input().split())

    sum_m = m1+m2
    sum_h = h1+h2

    if sum_m >= 60:
        sum_m -= 60
        sum_h += 1

    if sum_h >= 12:
        sum_h -= 12

    print(f"#{test_case} {sum_h} {sum_m}")
