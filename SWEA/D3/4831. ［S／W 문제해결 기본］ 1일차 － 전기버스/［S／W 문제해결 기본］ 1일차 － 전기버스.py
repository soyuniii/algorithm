T = int(input())
for test_case in range(1, T + 1):
    k,n,m = map(int, input().split()) #k만큼 이동가능, n번까지, 충전기는 m개
    charger = list(map(int, input().split())) # m개 충전소 위치

    bus = 0
    count = 0 # 최소 충전 횟수
    
    while bus + k < n:
        found = False
        #버스 최대거리부터 현재 위치까지 거꾸로 탐색
        for pos in range(bus+k, bus, -1):
            if pos in charger:
                bus = pos
                count += 1
                found = True
                break
                
        if not found:
            count = 0
            break                   
        
    print(f"#{test_case} {count}")

