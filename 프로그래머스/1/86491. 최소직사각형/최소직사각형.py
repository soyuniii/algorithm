def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w,h in sizes:
        long = max(w,h)
        short = min(w,h)
        
        max_w = max(max_w, long)
        max_h = max(max_h, short)
        
    return max_w * max_h
        
            
        