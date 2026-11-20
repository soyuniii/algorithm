def x(*args):
    total = 1
    for arg in args:
        if type(arg) is int:
            total *= arg
        else:
            return False
    return total


n_list = [1,2,'4',3]
result = x(*n_list)
print(result) if result else print("에러발생")