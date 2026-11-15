T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split()) #NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력
    table = [list(input().strip()) for _ in range(n)]
    result = ""
   
	#가로 기준
    for i in range(n):
        row = table[i]
        for j in range(n-m+1):
            sub = row[j:j+m]
            if sub == sub[::-1]:
                result = ''.join(sub)
                break
        if result:
                break
            
    # 세로 기준
    if not result:
        for j in range(n):
            for i in range(n-m+1):
                sub = [table[i+k][j] for k in range(m)]
                if sub == sub[::-1]:
                    result = ''.join(sub)
                    break
            if result:
                break
    print(f"#{test_case} {result}")
        
