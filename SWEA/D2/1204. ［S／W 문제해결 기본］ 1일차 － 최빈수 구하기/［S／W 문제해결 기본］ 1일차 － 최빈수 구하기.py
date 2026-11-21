T = int(input())

for test_case in range(1, T + 1):
    t = int(input())
    scores = list(map(int, input().split()))
    cnt = [0] * 101
    result = 0

    for score in scores:
        cnt[score] += 1

    for i in range(len(cnt)):
        if cnt[i] == max(cnt):
            result = i
        

    print(f"#{test_case} {result}")
