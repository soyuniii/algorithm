def solution(my_string):
    result = [0] * 52
    
    for str in my_string:
        if str.isupper():
            idx = ord(str) - ord('A')
            result[idx] += 1
        else:
            idx = ord(str) - ord('a') + 26
            result[idx] += 1
    
    return result
            