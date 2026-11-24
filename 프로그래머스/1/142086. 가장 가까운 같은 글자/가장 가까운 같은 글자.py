def solution(string):
    result = [-1]*len(string)
    last_pos = {}
    for i,s in enumerate(string):
        if s not in last_pos.keys():
            last_pos[s] = i
        else:
            result[i] = i - last_pos[s]
            last_pos[s] = i
    return result 
        
            
        