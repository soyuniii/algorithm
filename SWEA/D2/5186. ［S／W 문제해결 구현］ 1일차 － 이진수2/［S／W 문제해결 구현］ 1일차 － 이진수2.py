
T = int(input())

for test_case in range(1, T + 1):
    n = float(input())
    result = ""
    count = 0.5
    current = 0
    # 0.625
    # = 0.5 + 0.25 + 0.125 + ....
    # = 1 - 0 - 1
    while current != n:
        if (current + count) <= n:
            current += count
            result += "1"
        else:
            result += "0"

        count /= 2

    print(f"#{test_case} {result if len(result) <= 12 else 'overflow'}")







