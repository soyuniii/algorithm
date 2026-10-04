def solution(s):
    answer = len(s)
    
    if answer == 1:
        return 1
    
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        
        for j in range(step, len(s), step):
            sub = s[j:j+step]
            if prev == sub:
                count += 1
            else:
                compressed += (str(count) + prev) if count >= 2 else prev
                prev = sub
                count = 1
                
        compressed += (str(count) + prev) if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer