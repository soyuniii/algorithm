def solution(t, p):
    result = 0
    window = len(p)
    for i in range(len(t)-window+1):
        if int(t[i:i+window]) <= int(p):
            result += 1
            
    return result