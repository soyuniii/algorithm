T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split()) #n개 수열, m번 반복
    q = list(map(int, input().split()))
    # 맨앞pop 맨뒤로append -> 선형 큐
    
    for _ in range(m):
        first = q.pop(0)
        q.append(first)
        
    print(f"#{test_case} {q.pop(0)}")
    
    
