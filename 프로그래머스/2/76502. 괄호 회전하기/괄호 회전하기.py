def solution(s):
    answer = 0
    pair = {')':'(', '}':'{', ']':'['}
    
    # s를 왼쪽으로 x칸만큼 회전
    for x in range(len(s)):
        stack = []
        target = s[x:]+s[:x]
        is_valid = True
        
        for ch in target:
            if ch in pair.values():
                stack.append(ch)
            else:
                if not stack:
                    is_valid = False
                    break
                if stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    is_valid = False
                    break
        if not stack and is_valid:
            answer += 1
            
    return answer