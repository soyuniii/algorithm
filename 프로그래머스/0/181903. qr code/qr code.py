def solution(q, r, code):
    str = ''
    for i in range(len(code)):
        if i % q == r:
            str += code[i]
        else:
            continue
    return str