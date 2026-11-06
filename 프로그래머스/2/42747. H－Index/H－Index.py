def solution(citations):
    citations.sort()
    n = len(citations)
    
    for i in range(n):
        h_candidate = n-i
        
        if citations[i] >= h_candidate:
            return h_candidate
        
    return 0
            
    