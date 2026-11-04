def solution(s):
    result = ''
    idx = 0
    
    for char in s:

        if idx % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
            
        
        if char == ' ':
            idx = 0
        else:
            idx += 1
            
    return result
            