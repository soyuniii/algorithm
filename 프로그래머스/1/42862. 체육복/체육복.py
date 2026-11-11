def solution(n, lost, reserve):
    # 여벌 있는데 도난당한 학생 제거
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    # 체육복 빌려주기
    for r in set_reserve:
        if r-1 in set_lost:
            set_lost.remove(r-1)
        elif r+1 in set_lost:
            set_lost.remove(r+1)
            
    return n - len(set_lost)
    
    