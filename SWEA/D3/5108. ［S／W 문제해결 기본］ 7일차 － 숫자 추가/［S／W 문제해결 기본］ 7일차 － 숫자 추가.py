T = int(input())

for test_case in range(1, T + 1):
    n, m, l = map(int, input().split()) #수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L
    ls = list(map(int, input().split()))
    for _ in range(m):
        i, num = map(int, input().split())
        ls.insert(i, num)
    print(f"#{test_case} {ls[l]}")
        
    
    # 완성된 수열에서 인덱스 L의 데이터를 출력
