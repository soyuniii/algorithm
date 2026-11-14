def binary_search(p, target):
    l = 1
    r = p
    count = 0
    while l <= r:
        c = (l+r) // 2
        count += 1
        
        if c == target:
            return count
        elif c > target:
            r = c
        else:
            l = c
    return count

T = int(input())

for test_case in range(1, T + 1):
    #전체 쪽 수 P, A, B가 찾을 쪽 번호 Pa, Pb
    p, pa, pb = map(int, input().split())
	
    # a,b의 시도 횟수
    a = binary_search(p, pa)
    b = binary_search(p, pb)
    
    if a == b:
        print(f"#{test_case} 0")
    elif a > b:
        print(f"#{test_case} B")
    else:
        print(f"#{test_case} A")  
    
    
