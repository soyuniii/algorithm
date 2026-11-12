def solution(name):
    answer = 0 # 최소 조작 횟수
    n = len(name)
    
    # 상하 조작
    for char in name:
        answer += min(ord(char) - ord("A"),  ord("Z") - ord(char) + 1)
        
    # 좌우 이동
    min_move = n-1 # 오른쪽 직진 (기본값)
    
    for i, char in enumerate(name):
        next_idx = i+1
        while next_idx < n and name[next_idx] == "A":
            next_idx += 1
        
        min_move = min(min_move, i + n-next_idx + min(i, n-next_idx))
    answer += min_move  
    return answer