def solution(p):
    if not p:
        return ""
    
    def seperate_p(p):
        left = 0
        right = 0
        for i in range(len(p)):
            if p[i] == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                return p[:i+1], p[i+1:]
            
    def is_correct(string):
        count = 0
        for s in string:
            if s == '(':
                count += 1
            else:
                count -= 1
            
            if count < 0:
                return False
        return count == 0
    
    def reverse_u(u):
        result = ""
        for char in u:
            if char == '(':
                result += ')'
            else:
                result += '('
        return result
    
    u,v = seperate_p(p)
    if is_correct(u) == False:
        return '(' + solution(v) + ')' + reverse_u(u[1:-1])
    else:
        return u + solution(v)
            