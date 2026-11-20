T = int(input())

for test_case in range(1, T+1):
    s = input()
    if s.islower():
        print(f"#{test_case} {s} 는 소문자 입니다.")