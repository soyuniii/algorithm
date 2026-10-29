import re

def solution(myStr):
    answer = [x for x in re.split(r'[abc]', myStr) if x]
    
    if not answer: return ["EMPTY"] 
    return answer