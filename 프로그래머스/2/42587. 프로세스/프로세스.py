from collections import deque

def solution(priorities, location):
    q = deque([(i,p) for i,p in enumerate(priorities)])
    count = 0
    
    while q:
        curr = q.popleft()
        
        if any(curr[1] < other[1] for other in q):
            q.append(curr)
        else:
            count += 1
            if curr[0] == location:
                return count
            
        
    
    