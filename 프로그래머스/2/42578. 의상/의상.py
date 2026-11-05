def solution(clothes):
    hash_map = {}
    
    for name, kind in clothes:
        hash_map[kind] = hash_map.get(kind, 0) + 1
    
    answer = 1
    
    for count in hash_map.values():
        answer *= (count + 1)
    
    return answer - 1
        