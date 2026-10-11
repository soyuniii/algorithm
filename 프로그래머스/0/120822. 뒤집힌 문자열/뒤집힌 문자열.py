def solution(my_string):
    result = ""
    for i in range(1, len(my_string)+1):
        result += my_string[-i]
    return result